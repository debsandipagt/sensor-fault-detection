from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from src.exception import CustomException
from src.logger import logging
import sys
import os
from datetime import datetime

from src.components.data_ingestion import DataIngestion


# Add 'src' directory to Python path
#sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.pipeline.train_pipeline import TrainingPipeline
from src.pipeline.predict_pipeline import PredictionPipeline





app = Flask(__name__)

app.secret_key = 'a1b2c3d4e5f678901234567890abcdef1234567890abcdef1234567890abcdef'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/train")
def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()

        message = "Training Completed"
        return render_template('training_result.html', message=message)
        
    except Exception as e:
        raise CustomException(e, sys)
    
@app.route("/predict", methods=["GET","POST"])
def upload():
    try:
        if request.method == "POST":
            prediction_pipeline = PredictionPipeline(request)
            prediction_file_detail = prediction_pipeline.run_pipeline()

            # Create a unique file name for download by appending timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            download_filename = f"predicted_file_{timestamp}.csv"

            flash("Prediction completed and file downloaded.")

            logging.info("prediction completed. Downloading prediction file.")
            return send_file(prediction_file_detail.prediction_file_path,
                            download_name= prediction_file_detail.prediction_file_name,
                            as_attachment= True)
            #return render_template("end.html")


        else:
            return render_template('upload_file.html')
        
    except CustomException as e:
        # Flash the error message and redirect to the /predict page
        flash("Wrong data file selected. Please upload the correct file.")
        return redirect(url_for('upload'))
        
    except Exception as e:
        raise CustomException(e,sys)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

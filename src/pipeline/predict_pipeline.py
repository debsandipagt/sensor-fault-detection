import shutil
import os, sys
import pandas as pd
import pickle
from flask import request
from datetime import datetime

from src.logger import logging
from src.exception import CustomException
from src.constant import *
from src.utils.main_utils import MainUtils

from dataclasses import dataclass

@dataclass
class PredictPipelineConfig:
    predict_output_dir_name: str = "predictions"
    prediction_file_name: str = f"predicted_file_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"    
    model_file_path: str = os.path.join(artifact_folder, "model.pkl")
    processor_path: str = os.path.join(artifact_folder, "preprocessor.pkl")
    prediction_file_path: str = os.path.join(predict_output_dir_name, prediction_file_name)

class PredictionPipeline:

    def __init__(self, request):
        self.request = request
        self.utils = MainUtils()
        self.predict_pipeline_config = PredictPipelineConfig()

    def save_input_files(self) -> str:
        """
        Method Name :   save_input_files
        Description :   This method saves the input file to the prediction artifacts directory. 
            
        Output      :   input dataframe
        On Failure  :   Write an exception log and then raise an exceptionS
            
        Version     :   1.2
        Revisions   :   moved setup to cloud
        """
        try:
            #Creating the file
            pred_file_input_dir = "prediction_artifacts"
            # Ensure the directory exists
            
            os.makedirs(pred_file_input_dir, exist_ok=True)

            input_csv_file = self.request.files['file']
            # pred_file_path = os.path.join(pred_file_input_dir, input_csv_file.filename)
            # logging.info(f"File path: {pred_file_path}")
            # input_csv_file.save(pred_file_path)

            # Generate a unique file name by appending date and time
            original_filename = input_csv_file.filename
            base_name, ext = os.path.splitext(original_filename)
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_filename = f"{base_name}_{current_time}{ext}"
            
            pred_file_path = os.path.join(pred_file_input_dir, unique_filename)
            logging.info(f"Saving file to: {pred_file_path}")

            input_csv_file.save(pred_file_path)

            return pred_file_path

        except Exception as e:
            raise CustomException(e, sys)
        
    def predict(self, features):

        try:
            model = self.utils.load_object(self.predict_pipeline_config.model_file_path)
            processor = self.utils.load_object(file_path=self.predict_pipeline_config.processor_path)
            transformed_x = processor.transform(features)
            preds = model.predict(transformed_x)

            return preds

        except Exception as e:
            raise CustomException(e, sys)
        
    def get_predicted_dataframe(self, input_dataframe_path: pd.DataFrame) -> None:

        """
            Method Name :   get_predicted_dataframe
            Description :   this method returns the dataframw with a new column containing predictions

            
            Output      :   predicted dataframe
            On Failure  :   Write an exception log and then raise an exception
            
            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            prediction_colum_name: str = TARGET_COLUMN
            input_dataframe: pd.DataFrame = pd.read_csv(input_dataframe_path)
            input_dataframe = input_dataframe.drop(columns="Unnamed: 0") if "Unnamed: 0" in input_dataframe.columns else input_dataframe
            predictions = self.predict(input_dataframe)

            input_dataframe[prediction_colum_name] = [pred for pred in predictions]
            targe_colum_mapping = {0: "bad", 1: "good"}
            input_dataframe[prediction_colum_name] = input_dataframe[prediction_colum_name].map(targe_colum_mapping)

            os.makedirs(self.predict_pipeline_config.predict_output_dir_name, exist_ok=True)
            input_dataframe.to_csv(self.predict_pipeline_config.prediction_file_path)
            #input_dataframe.to_csv(self.predict_pipeline_config.prediction_file_path, index=False)


            logging.info("predictions completed. ")

        except Exception as e:
            raise CustomException(e, sys)
        
    def run_pipeline(self):
        try:
            input_csv_path = self.save_input_files()
            self.get_predicted_dataframe(input_csv_path)

            # Delete the input file after prediction is done
            if os.path.exists(input_csv_path):
                os.remove(input_csv_path)
                logging.info(f"Deleted input file: {input_csv_path}")
            
            return self.predict_pipeline_config

        except Exception as e:
            raise CustomException(e, sys)




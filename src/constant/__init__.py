import os


AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = "waferfault_db"
MONGO_COLLECTION_NAME = "waferfault"

TARGET_COLUMN = "quality"
#MONGO_DB_URL="mongodb+srv://snshrivas:Snshrivas@cluster0.u46c4.mongodb.net/?retryWrites=true&w=majority"
MONGO_DB_URL="mongodb+srv://mongodb:mongodb@cluster0.ahyxq.mongodb.net/?retryWrites=true&w=majority"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder =  "artifacts"
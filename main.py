from src.logger import logging
from src.exception import CustomException
from src.components import data_ingestion ,data_transformation,model_trainer
import sys


def main():
  
    logging.info("we have entered in the main function")
    DataIngestion=data_ingestion.DataIngestion()
    Train_Path,Test_Path=DataIngestion.initiate_data_ingestion()
    DataTransformation=data_transformation.DataTransformation()
    train_arr,test_arr,_=DataTransformation.initiate_data_transformation(Train_Path,Test_Path)
    ModelTrainer=model_trainer.ModelTrainer()
    ModelTrainer.initiate_model_trainer(train_arr,test_arr)


       





if __name__=="__main__":
    logging.info("logging is started")
    main()
    

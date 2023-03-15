from src.logger import logging
from src.exception import CustomException
from src.components import data_ingestion 
import sys


def main():
  
    logging.info("we have entered in the main function")
    DataIngestion=data_ingestion.DataIngestion()
    DataIngestion.initiate_data_ingestion()




       





if __name__=="__main__":
    logging.info("logging is started")
    main()
    

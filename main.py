from src.logger import logging
from src.exception import CustomException
import sys


def main():
    try:
        logging.info("we have entered in the main function")
        a=6/0
    except Exception as e:
        raise CustomException(e, sys)









if __name__=="__main__":

    main()
    logging.info("logging is started")

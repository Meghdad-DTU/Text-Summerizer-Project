import sys
from textSummerizer.config.configuration import configurationManeger
from textSummerizer.components.data_validation import DataValiadtion
from textSummerizer.logger import logging
from textSummerizer.exception import CustomException


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configurationManeger()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()

STAGE_NAME = "Data Validation Stage"

if __name__ == '__main__':
    try:        
        logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
        obj = DataValidationTrainingPipeline()
        obj.main()
        logging.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<<<')
    
    except Exception as e:
        raise CustomException(e, sys)
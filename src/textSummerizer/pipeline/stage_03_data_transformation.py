import sys
from textSummerizer.config.configuration import configurationManeger
from textSummerizer.components.data_transformation import DataTransformation
from textSummerizer.logger import logging
from textSummerizer.exception import CustomException


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configurationManeger()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()

STAGE_NAME = "Data Transformation Stage"

if __name__ == '__main__':
    try:        
        logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logging.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<<<')
    
    except Exception as e:
        raise CustomException(e, sys)
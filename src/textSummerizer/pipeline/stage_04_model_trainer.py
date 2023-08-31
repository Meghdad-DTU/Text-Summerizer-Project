import sys
from textSummerizer.config.configuration import configurationManeger
from textSummerizer.components.model_trainer import ModelTrainer
from textSummerizer.logger import logging
from textSummerizer.exception import CustomException


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configurationManeger()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

STAGE_NAME = "Model Training Stage"

if __name__ == '__main__':
    try:        
        logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
        obj = ModelTrainingPipeline()
        obj.main()
        logging.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<<<')
    
    except Exception as e:
        raise CustomException(e, sys)
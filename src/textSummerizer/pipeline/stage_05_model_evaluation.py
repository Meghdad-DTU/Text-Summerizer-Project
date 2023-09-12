import sys
from textSummerizer.config.configuration import configurationManeger
from textSummerizer.components.model_evaluation import ModelEvaluation
from textSummerizer.logger import logging
from textSummerizer.exception import CustomException


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configurationManeger()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config= model_evaluation_config)
        model_evaluation_config.evaluate()

STAGE_NAME = "Model Evaluation Stage"

if __name__ == '__main__':
    try:        
        logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
        obj = ModelEvaluationPipeline()
        obj.main()
        logging.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<<<')
    
    except Exception as e:
        raise CustomException(e, sys)
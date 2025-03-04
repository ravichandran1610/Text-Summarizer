from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline


STAGE_NAME = 'Data Ingestion'
try:
    logger.info(f'>>>>> Stage: {STAGE_NAME} started <<<<<<')
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f'>>>>> Stage: {STAGE_NAME} completed <<<<<< \n\nX===========================X')

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation'
try:
    logger.info(f'>>>>> Stage: {STAGE_NAME} started <<<<<<')
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f'>>>>> Stage: {STAGE_NAME} completed <<<<<< \n\nX===========================X')

except Exception as e:
    logger.exception(e)
    raise e


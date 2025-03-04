from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline


STAGE_NAME = 'Data Ingestion'

try:
    logger.info(f'>>>>> Stage: {STAGE_NAME} started <<<<<<')
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f'>>>>> Stage: {STAGE_NAME} completed <<<<<< \n\nX===========================X')

except Exception as e:
    logger.exception(e)
    raise e

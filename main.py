from cnnClassifier.pipeline.stage_01_dataingestion import DataIngestionTrainingPipeline
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion phase"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

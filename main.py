from cnnClassifier.pipeline.stage_01_dataingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier import logger

STAGE_NAME_1 = "Data Ingestion phase"

try:
    logger.info(f">>>>>> stage {STAGE_NAME_1} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME_1} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_2 = "Prepare Base Model Training"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME_2} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME_2} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

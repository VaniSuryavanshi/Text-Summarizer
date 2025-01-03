from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger
from pathlib import Path

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Initialize ConfigurationManager
        config_manager = ConfigurationManager(
            config_filepath=Path("/Users/vanisuryavanshi/Text-Summarizer/config/config.yaml"),
            params_filepath=Path("/Users/vanisuryavanshi/Text-Summarizer/params.yaml")
        )
        # Get the data ingestion configuration
        data_ingestion_config = config_manager.get_data_ingestion_config()

        # Initialize the DataIngestion class with the config
        data_ingestion = DataIngestion(config=data_ingestion_config)

        # Call the methods
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

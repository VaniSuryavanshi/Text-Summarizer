from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger
from pathlib import Path

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        config_manager = ConfigurationManager(
            config_filepath=Path("/Users/vanisuryavanshi/Text-Summarizer/config/config.yaml"),
            params_filepath=Path("/Users/vanisuryavanshi/Text-Summarizer/params.yaml")
        )
        data_validation_config = config_manager.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()
import json
import logging

# Standard
from pathlib import Path

# Local
from watson_doc_understanding import (
    DocumentBytes,
    File,
    fetch_du_model,
    load_du_models_from_config,
    pre_validate_models_dir,
)

from watson_doc_understanding.data_model.ocr import OCRPrediction

from watson_doc_understanding.workflows.document_processing.document_processor import DocProcessor

logger = logging.getLogger("DU.EXAMPLE")
logger.setLevel(logging.DEBUG)


def load_models_for_example():
    # This example assumes the models have already been installed into a directory,
    # and Caikit is configured to discover that directory.  One way to configure
    # the models directory is to assign the path to the RUNTIME_LOCAL_MODELS_DIR
    # environment variable.
    # For faster startup, we can control which models will load.  In this example,
    # we will invoke "iocr_and_tables", which will depend on "ocr_iocr", "table_extraction_gte",
    # and "language_detection".  (At this time, DU does not automatically determine model
    # dependencies, which is a known short-coming).  The model names must correspond to the
    # directory names in the models folder.
    models_config = {
        "models": {
            "invoice_kvp": {"local": False},
            "iocr_and_tables": {"local": False},
            "iocr_kvp": {"local": True},
            "ocr_iocr": {"local": True},
            "ocr_str": {"local": False},
            "table_extraction_gte": {"local": False},
            "language_detection": {"local": True},
            "doc_processing": {"local": True},
        }
    }
    # This is just an early check that the model directory can be discovered, and
    # the models that are specified are present there.
    logger.info("Doing basic model directory validation")
    pre_validate_models_dir(models_config)
    # And now we ask DU/Caikit to load the models as appropriate.  Note in more advanced
    # configurations, the models may be decomposed into separate services and called
    # via gRPC.
    logger.info("Invoking load_du_models_from_config")
    load_du_models_from_config(models_config)


def main():
    """
    This example processes an image through the DU IOCRAndTablesWorkflow model,
    and processes text and tables into a "fused" structure consumable by downstream processing.
    """
    # First load in needed models into DU, assuming the models have already been installed.
    load_models_for_example()

    # Set up a path object to an image, and put it into a DocumentBytes object.
    this_folder = Path(__file__).parent
    image_path = this_folder.joinpath("1.jpg")
    assert image_path.exists()

    # The document bytes object packages a document into a DU data model format
    # that may be passed to the model.
    doc_bytes = DocumentBytes(
        File(data=image_path.read_bytes(), filename=image_path.name)
    )

    # Ask the IOCRAndTablesWorkflow model to perform its inference.
    logger.info("IOCRAndTablePrediction inference starting")
    docProcessor: DocProcessor = fetch_du_model(DocProcessor)
   
    output= docProcessor.run(doc_bytes, languages_list=["eng"], auto_rotation_correction=False, pre_processing=None)
    #output_dict:dict = output.to_dict()
    output_json = json.loads(output.processing_output)


    with open("iocr.json", "w", encoding="utf-8") as fp:
        json.dump(output_json, fp, ensure_ascii=False, indent=4)
    
    #print(output.to_json())


if __name__ == "__main__":
    main()
from src.manager.load_manager import load_pdf_manager
import logging

# setup logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_pdf_controller(file_path):
    """
    Controller for loading a PDF.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        dict: Response from the load_pdf_manager.
              Typically contains the status, message, or extracted data.
    """
    try:
        logger.info(f"Received request to load PDF from path:{file_papythonth}")

        #validate the path

        if not file_path.endswith ('.pdf'):
            raise ValueError("Invalid file format. Please provide a PDF file. ")
        

        #delegate to the manager

        response = load_pdf_manager(file_path)
        logger.info(f"Sucessfully processed PDF:{file_path}")
        return response
    
    except Exception as e:
        logger.error(f"Error loading PDF:{e}")
        return{"status":"Error","message":str(e)}
    
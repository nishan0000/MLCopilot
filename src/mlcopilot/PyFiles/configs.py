import os
ALLOWED_EXTENSIONS = ['.csv', '.xls', '.xlsx']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENGINE_FILES_PATH = os.path.join(BASE_DIR)#'..','engine', 'files')

FILE_PATH = os.path.abspath(ENGINE_FILES_PATH) + os.sep

output_files = 'OutputFiles'
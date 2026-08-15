## Production system mein jab kuch unexpected hota hai, 
# logs help you reconstruct what happened and locate the failure.
# basically ye decide kar raha hai ki ye information kis format mein 
# aur kis level par log file mein record hogi.

import logging
import os
from datetime import datetime


## entire log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


## logs path that im actually creating in the project directory

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(logs_path, exist_ok = True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s- %(message)s",
    level = logging.INFO,
)


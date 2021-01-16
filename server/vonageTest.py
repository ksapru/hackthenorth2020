import vonage

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

client = vonage.Client(
    application_id=os.environ.get("VONAGE_APPLICATION_ID"),
    private_key=os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH"),
)


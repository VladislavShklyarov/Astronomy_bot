import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Environment variables were not loaded because the ".env" file is missing.'
         ' Please make sure the file is available and try again.')
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
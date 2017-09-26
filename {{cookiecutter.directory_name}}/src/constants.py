import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# Log Level
LOG_LEVEL = os.getenv('LOG_LEVEL') or os.environ['LOG_LEVEL']

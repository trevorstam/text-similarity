import os
from dotenv import load_dotenv
load_dotenv()

PGHOST = os.getenv('PGHOST')
PGDBNAME = os.getenv('PGDBNAME')
PGUSERNAME = os.getenv('PGUSERNAME')
PGPASSWORD = os.getenv('PGPASSWORD')


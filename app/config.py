import os
import dotenv
dotenv.load_dotenv()

# CSRF_ENABLED = True
# SECRET_KEY = os.getenv('SECRET_KEY', '')
assert os.getenv('API_KEY', ''), 'There was not API_KEY'
API_KEY = os.getenv('API_KEY', '')

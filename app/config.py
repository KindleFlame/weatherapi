import os
import dotenv
dotenv.load_dotenv()

# CSRF_ENABLED = True
# SECRET_KEY = os.getenv('SECRET_KEY', '')
API_KEY = os.getenv('API_KEY', '')

# check =
if not API_KEY:
    assert False, 'There was not API_KEY'





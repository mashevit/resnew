from decouple import Config

# Create a Config object
config = Config()

# Load configuration values from the .env file
config.read(".env")

# Fetch global variables from the .env file
SECRET_KEY = config.get("SECRET_KEY")
DEBUG = config.getboolean("DEBUG")
DATABASE_URL = config.get("DATABASE_URL")

# You can now use these variables in your Python code
print(SECRET_KEY)
print(DEBUG)
print(DATABASE_URL)
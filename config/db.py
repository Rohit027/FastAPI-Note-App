import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the MONGO_URI from the environment
MONGO_URI = os.getenv("MONGO_URI")

# Create the MongoDB connection
conn = MongoClient(MONGO_URI)

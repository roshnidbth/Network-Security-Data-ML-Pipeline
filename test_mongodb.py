
from pymongo import MongoClient

uri = "mongodb+srv://roshniim01_db_user:HFuTVxZ90Cs4WUOc@cluster0.lg87qjb.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
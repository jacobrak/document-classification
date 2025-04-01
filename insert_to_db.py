import os
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["story_database"]  # Database name
collection = db["short_stories"]

data_folder = "data"

for filename in os.listdir(data_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(data_folder, filename), "r", encoding="utf-8") as file:
            text = file.read()
            classification =  


        # Insert into MongoDB
        collection.insert_one({"filename": filename, "text": text})
print("done")
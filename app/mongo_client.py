from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

class AtlasClient():
    def __init__(self):
        ATLAS_URI = os.getenv("ATLAS_URI")
        client = MongoClient(ATLAS_URI)

        db = client['checklist_db']
        self.checklists = db["checklists"]

    def add_checklist(self, title, body):
        insert_result = self.checklists.insert_one({
            "title": title,
            "body": body 
        })

        return insert_result.inserted_id

    def fetch_checklist(self, id):
        return self.checklists.find_one(ObjectId(id))

if __name__ == "__main__":
    client = AtlasClient()
    #id = client.add_checklist("this is a title", "this is a body")
    #print(id)
    print(client.fetch_checklist("668eb7d48a9f3d7a3f26bdd0")["title"])
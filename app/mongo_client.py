from pymongo import MongoClient
from bson import ObjectId

#print(movies.find()[0])
#print(movies.find_one({"title": "The Great Train Robbery"}))

class AtlasClient():
    def __init__(self):
        ATLAS_URI = "mongodb+srv://jasonxwang9:H0vkAO71JwGHJJI9@testcluster.0gygauk.mongodb.net/?retryWrites=true&w=majority&appName=testcluster"

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
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

class AtlasClient():
    def __init__(self):
        ATLAS_URI = os.getenv("ATLAS_URI")
        client = MongoClient(ATLAS_URI)

        self.db = client['artheals']

    def real_category(self, category):
        if category in ["characters", "animals", "flowers", "other"]:
            return True
        print("not a categoryadjfoisdjf")
        return False

    def add_card_list(self, cards, category):
        if self.real_category(category):
            insert_result = self.db[category].insert_one({
                "cards" : cards
            })

            return insert_result.inserted_id

    def get_card_list(self, category):
        if self.real_category(category):
            a = list(self.db[category].find())[0]
            return a["cards"]

    def update_card_list(self, category, card_list):
        if self.real_category(category):
            ret = self.db[category].update_one(
                filter={},
                update={
                    "$set" : {
                        "cards" : card_list
                    }
                }
            )
            return ret
        

if __name__ == "__main__":
    client = AtlasClient()
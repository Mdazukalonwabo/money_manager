import pymongo


class Database:
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['moneymanager']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find_all(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        print(collection)
        print(query)
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, new_details):
        return Database.DATABASE[collection].update_one(query, new_details, upsert=False)

from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)
client.admin.authenticate("root", "root")
db = client["vega"]["news"]

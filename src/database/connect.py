from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")  #? conexion a la base de datos

global db
db = client["pruebaIA"]                           #? seleccion de la base de datos    

def getCollection(colect):
    return db[colect]

def insert(colect, document):
    result = colect.insert_one(document)
    return result.inserted_id

def getAll(colect):
    results = colect.find()
    return list(results)

def getSome(colect, query):
    results = colect.find(query)
    return list(results)
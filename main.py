import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("restorane-db2e2-ed59efaf84be.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

class UsersAdd:
    def Usersadd(user):
        collection = db.collection('Users') 
        collection.document().set(user.returnUser())
        

    def Getusers():
        collection = db.collection('Users')
        res = collection.get()
        return res
    def UpdateUser(userid,user):
        collection = db.collection('Users').document(userid)
        res = collection.update(user.returnUser())
        return res
    def GetUserInfo(mail):
        collection = db.collection('Users')
        res = collection.where('mail','==',mail).get()
        return res
class ZakazAdd:
    def ZakazAdd(zakaz):
        collection = db.collection('Zakaz') 
        collection.document().set(zakaz.returnZakaz())
        

    def GetZakaz():
        collection = db.collection('Zakaz')
        res = collection.get()
        return res
    def GetUserZakaz(mail):
        collection = db.collection('Zakaz')
        res = collection.where('mailUser','==',mail).get()
        return res
    

class Ingridient:
    def IngridAdd(ingridientic):
        collection = db.collection('ingridientic') 
        collection.document().set(ingridientic.returnIngrid())
        

    def GetIngrid():
        collection = db.collection('ingridientic')
        res = collection.get()
        return res
    def UpdateIngrid(user):
        collection = db.collection('ingridientic').document("IafyIUhx6njrIPMrcyXq")
        res = collection.update(user.returnIngrid())
        return res
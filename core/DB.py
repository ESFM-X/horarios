import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./private/horario-f7ff5-firebase-adminsdk-xebih-c86b730d5a.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


import firebase_admin

import os

import json

from firebase_admin import credentials, firestore

cred = credentials.Certificate(os.getcwd()+'\cred\cred.json')

firebase_admin.initialize_app(cred)

db = firestore.client()
print( 'checking for json files in : '+os.getcwd()+'\jsonFiles')

for filename in os.listdir(os.getcwd()+'\jsonFiles'):

    if filename.endswith('.json'):

        collectionName = filename.split('.')[0] # filename minus ext will be used as collection name
        
        f = open( os.getcwd()+'\jsonFiles\\' +filename, 'r')

        docs = json.loads(f.read())

        for doc in docs:

            id = doc.pop('id', None)

            if id:

                db.collection(collectionName).document(id).set(doc, merge=True)

            else:

                db.collection(collectionName).add(doc)
        print('Success, Document uploaded to firestore')
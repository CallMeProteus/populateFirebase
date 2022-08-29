import firebase_admin

import os

import json

from firebase_admin import credentials, firestore

cred = credentials.Certificate("path to credentials json file")

firebase_admin.initialize_app(cred)

db = firestore.client()

for filename in os.listdir('path where json files to be uploaded is located'):

    if filename.endswith('.json'):

        collectionName = filename.split('.')[0] # filename minus ext will be used as collection name

        f = open( filename, 'r')

        docs = json.loads(f.read())

        for doc in docs:

            id = doc.pop('id', None)

            if id:

                db.collection(collectionName).document(id).set(doc, merge=True)

            else:

                db.collection(collectionName).add(doc)
        print('Success, Document uploaded to firestore')
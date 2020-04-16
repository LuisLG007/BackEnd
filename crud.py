import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
import string

# Use a service account
cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
ids = []
def delete_collection(coll_ref, batch_size):
    docs = coll_ref.limit(batch_size).get()
    deleted = 0

    for doc in docs:
        print(u'Deleting doc {} => {}'.format(doc.id, doc.to_dict()))
        doc.reference.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)

def read(collection):
    users_ref = db.collection(collection)
    docs = users_ref.stream()    
    count = 0
    for doc in docs:
        #print(u'{} => {}'.format(doc.id, doc.to_dict()))
        ids.append(doc.id)
        count = count + 1
    #print("Total",count)
    return (ids)

def create(collection, data):
    doc_ref = db.collection(collection)
    doc_ref.add(data)    
    print("Data added successfully")

def update(collection, document, data):
    doc_ref = db.collection(collection).document(document)
    doc_ref.update(data)

def delete(collection, document):
    db.collection(collection).document(document).delete()


#read('Chiapas')
#create('user')
#update('user','chwYcnlz87qvHvhKkDVb')
#delete('user','chwYcnlz87qvHvhKkDVb')
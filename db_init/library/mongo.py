from pymongo import MongoClient
from pymongo.database import Database

from library.mongoentries.products import ALL_WASHING_MASCHINES



def init_mongo_db(MONGO_HOST, MONGO_PORT, DB_NAME, ROOT_PASSWORD, USER, USER_PASSWORD):
  root_connection = MongoClient(f'mongodb://{MONGO_HOST}:{MONGO_PORT}/')

  root_db = root_connection.admin

  root_user = root_db.command('usersInfo', 'root')  
  if len(root_user.get('users', [])) > 0:
     print("Root already exists")
     return
  root_db.command('createUser', 'root', pwd=ROOT_PASSWORD, roles=["userAdminAnyDatabase", "dbAdminAnyDatabase", "readWriteAnyDatabase"])
  root_db.command("updateUser", "root", pwd=ROOT_PASSWORD)
  root_db.command(
      "createUser", USER, pwd=USER_PASSWORD, 
      roles=[
          { "role":"readWrite","db":f"{DB_NAME}"}
        ]
      )
  # Switch to user
  root_connection.close()


def create_blog_entries(MONGO_HOST, MONGO_PORT, DB_NAME, COLLECTION, USER, USER_PASSWORD):
    user_connection = MongoClient(f'mongodb://{USER}:{USER_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/')
    db: Database = getattr(user_connection, f'{DB_NAME}')
    collection = db[COLLECTION]

    # Check if entries exist already:
    product = collection.find_one({"productId": 1})
    if product:
       print("Products already exist")
       return

    



    result = collection.insert_many(ALL_WASHING_MASCHINES)

    user_connection.close()

from tinydb import TinyDB, Query
from tinydb.table import Document


class UsersDB:
    def __init__(self):
        db = TinyDB('db/users.json', indent=4)
        self.users = db.table('users')

    def is_user(self, user_id):
        return self.users.contains(doc_id=user_id)

    def add_user(self, user_id, firstname, lastname, username):
        if self.is_user(user_id):
            return False
        else:
            doc = Document(
                value={
                    "firstname": firstname,
                    "lastname": lastname,
                    "username": username
                },
                doc_id=user_id
            )
            self.users.insert(doc)
            return True
    
    def get_all_users(self):
        return self.users.all()


class SmartphonesDB:
    def __init__(self):
        self.db = TinyDB('db/smartphones.json', indent=4)

    def get_brends(self):
        return self.db.tables()

    def get_smartphones(self, brend):
        table = self.db.table(brend)
        return table.all()

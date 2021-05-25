
from .dbreqs import users, meta, engine


class AddData:
    def add_new_user(self, data):
        insert =  users.insert()
        insert = users.insert().values(userid=data['userid'],
                                       fullname=data['fullname'],
                                       username=data["username"],
                                       reg_date=data["reg_date"],
                                       parrent_refferal=data["parrent_refferal"],
                                       accept_days=data["accept_days"],
                                       last_link=data["last_link"],
                                       refferals=data["refferals"],
                                       test_period=data["test_period"]
                                       )
        conn = engine.connect()
        result = conn.execute(insert)

    def update_test_period_data(self, userid):
        self.user_id = userid
        update = users.update()
        update = users.update().where(users.c.userid == userid).values(test_period="accept", accept_days=7)
        conn = engine.connect()
        conn.execute(update)
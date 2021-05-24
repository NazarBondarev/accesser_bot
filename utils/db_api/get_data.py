from .dbreqs import users, meta, engine
from sqlalchemy.sql import alias, select




class GetData:
    def check_user(self, data):
        st = users.alias("a")
        conn = engine.connect()
        s = select([st]).where(st.c.userid == data['userid'])
        result = conn.execute(s).fetchone()
        return result

    def get_all_data(self) -> object:
        conn = engine.connect()
        u = users.select()
        result = conn.execute(u)
        users_detail = {}
        for row in result:
            users_detail[row[1]] = {"id": row[0], "userid": row[1], "fullname": row[2], "username": row[3],
                                    "reg_date": row[4], "parrent_refferal": row[5], "accept_days": row[6],

                                    "last_link": row[7], "refferals": row[8], "test_period": row[9]}

        print(type(users_detail))
        return users_detail


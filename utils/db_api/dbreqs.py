from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime

meta = MetaData()
engine = create_engine('sqlite:///data/database/dump.db', echo = True)

users = Table(
    'users', meta,
    Column("id", Integer, nullable=False, unique=True, primary_key=True, autoincrement=True),
    Column("userid", Integer, nullable=False, unique=True),
    Column("fullname",String),
    Column("username",String),
    Column("reg_date", DateTime),
    Column("parrent_refferal", Integer),
    Column("accept_days", Integer),
    Column("last_link", String),
    Column("refferals",String),
    Column("test_period", String)
)


meta.create_all(engine)



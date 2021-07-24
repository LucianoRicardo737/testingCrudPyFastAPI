from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://user:password@localhost:3306/storedb")

meta = MetaData()



conn = engine.connect()
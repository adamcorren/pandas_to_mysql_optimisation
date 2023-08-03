import sample_df
from sqlalchemy.orm import sessionmaker
import pandas as pd
import sqlalchemy
import time


def get_data():
    data = sample_df.create_test_df(1000000)
    return data


def connect_to_mysql_db():
    connection_string = "mysql+mysqlconnector://user:password@host/database"
    engine = sqlalchemy.create_engine(connection_string)
    return engine


def insert(df, engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    df.to_sql('data', engine, index=False, if_exists="append")

    session.commit()
    session.close()


def main():
    df = get_data()
    sizes = [100, 1000, 10000, 100000, 250000, 500000, 1000000]
    for s in sizes:
        start_time = time.time()
        df = df.sample(s, replace=True)
        engine = connect_to_mysql_db()
        insert(df, engine)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"{s} rows runtime: {runtime:.5f} seconds")


main()

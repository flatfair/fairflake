import configparser
import os

from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine


def get_config():
    config = configparser.ConfigParser()
    config.read(os.path.expanduser("~/.snowsql/config"))
    return config


def get_value(conf, conn, value: str):
    try:
        return conf[f"connections.{conn}"][value]
    except KeyError:
        return conf["connections"][value]


def get_connection(connection_name: str):
    conf = get_config()

    account = get_value(conf, connection_name, "accountname")
    region = get_value(conf, connection_name, "region")
    username = get_value(conf, connection_name, "username")
    password = get_value(conf, connection_name, "password")
    dbname = get_value(conf, connection_name, "dbname")
    warehouse = get_value(conf, connection_name, "warehousename")
    role = get_value(conf, connection_name, "role")

    engine = create_engine(
        URL(
            account=account,
            region=region,
            user=username,
            password=password,
            database=dbname,
            warehouse=warehouse,
            role=role,
        )
    )

    return engine.connect()

from pandas import read_sql_table


def table_to_csv(connection, table_name: str, file_name):
    spl = table_name.split(".")
    schema = spl[0] if len(spl) > 1 else None

    df = read_sql_table(spl[-1], connection, schema=schema)
    df.to_csv(file_name, index=False)

    connection.close()

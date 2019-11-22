from click import echo


def upload(connection, file_name, stage="~", path=""):
    qry = f"PUT file://{file_name} @{stage}/{path};"
    echo(qry)
    connection.execute(qry)

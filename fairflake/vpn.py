from dns import resolver
from click import echo
from .config import get_config, get_value


def route_traffic(connection_name: str):
    conf = get_config()
    account = get_value(conf, connection_name, "accountname")
    region = get_value(conf, connection_name, "region")
    endpoint = f"{account}.{region}.snowflakecomputing.com"
    dns_answers = resolver.query(endpoint)
    hosts = [i.address for i in dns_answers.rrset.items]

    for h in hosts:
        echo(f"sudo route -n add -net {h}/32 172.27.240.1")

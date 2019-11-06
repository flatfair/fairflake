import click

import fairflake.config as c
import fairflake.unload as u
import fairflake.vpn as v


@click.option("-c", "--connection", help="Snowsql connection name")
@click.group()
@click.pass_context
def cli(ctx, connection=None):
    ctx.ensure_object(dict)
    ctx.obj["connection"] = connection or "development"


@click.argument("file_name", type=click.Path(dir_okay=False))
@click.argument("table_name")
@cli.command()
@click.pass_context
def table_to_csv(ctx, table_name: str, file_name):
    conn = c.get_connection(ctx.obj["connection"])
    u.table_to_csv(conn, table_name, file_name)


@cli.command()
@click.pass_context
def route_vpn(ctx):
    v.route_traffic(ctx.obj["connection"])

import click

import fairflake.config as c
import fairflake.unload as unl
import fairflake.upload as upl
import fairflake.vpn as v


@click.option("-c", "--connection", help="Snowsql connection name", default="development")
@click.group()
@click.pass_context
def cli(ctx, connection):
    ctx.ensure_object(dict)
    ctx.obj["connection"] = connection


@click.argument("file_name", type=click.Path(dir_okay=False))
@click.argument("table_name")
@cli.command()
@click.pass_context
def table_to_csv(ctx, table_name: str, file_name):
    conn = c.get_connection(ctx.obj["connection"])
    unl.table_to_csv(conn, table_name, file_name)


@cli.command()
@click.pass_context
def route_vpn(ctx):
    v.route_traffic(ctx.obj["connection"])


@click.argument("file_name", type=click.Path(dir_okay=False))
@click.option("-s", "--stage", help="Snowflake stage", default="~")
@click.option("-p", "--path", help="Target folder in Snowflake stage", default="")
@cli.command()
@click.pass_context
def upload(ctx, file_name, stage, path):
    conn = c.get_connection(ctx.obj["connection"])
    upl.upload(conn, file_name, stage, path)

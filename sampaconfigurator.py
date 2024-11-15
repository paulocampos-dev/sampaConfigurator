import click
import getRegister


@click.group()
def cli() -> None:
    pass


cli.add_command(getRegister.getregx)

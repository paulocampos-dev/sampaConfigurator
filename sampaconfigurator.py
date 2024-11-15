import click

import daq


@click.group()
def cli() -> None:
    pass


cli.add_command(daq.daq_read)

import click

import fpga


@click.group()
def cli() -> None:
    pass


cli.add_command(fpga.fpga_read)

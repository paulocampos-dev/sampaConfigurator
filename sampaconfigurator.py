import click

import control
import fpga


@click.group()
def cli() -> None:
    pass


cli.add_command(fpga.fpga_read)

cli.add_command(control.serial_out)

import click
from utils import serial_utils, daq
from constants import CNC_REG_SIZE, DM_REG_SIZE


@click.command()
@click.option(
    "--port",
    required=True,
    help="Serial port to communicate with (e.g., COM1, /dev/ttyUSB0).",
)
@click.option(
    "--baudrate",
    default=115200,
    show_default=True,
    help="Baud rate for the serial communication.",
)
@click.option(
    "--address",
    type=click.IntRange(0, 0xFFFF),
    help="16-bit register address to read from",
)
@click.option(
    "--cnc",
    help="Indicates that the register will be an Comand and Control register",
    is_flag=True,
)
@click.option(
    "--dm",
    help="Indicates that the register will be an Data Manager register",
    is_flag=True,
)
@click.option(
    "--all",
    "-A",
    "read_all",
    is_flag=True,
    help="Read all the registers, it can be used with --cnc/--dm options to read all CNC/DM registers",
)
def fpga_read(
    port: str, address: int, baudrate: int, read_all: bool, cnc: bool, dm: bool
) -> list[tuple[bool, int]]:
    """
    Reads data from the FPGA at the specified address.

    Parameters:
        port (str): The name of the port (e.g., 'COM3' for Windows or '/dev/ttyUSB0' for Linux).
        address (int): The address of the register to read in decimal base.
        read_all (bool): Flag that defines if All register will be read.
        cnc (bool): Flag that defines if the address is for a CNC register
        dm (bool): Flag that defines if the address is for a DM register
    Returns:
        Tuple[bool, int]: A tuple where the first element indicates success (True/False),
                          and the second is the data read from the DAQ (32-bit unsigned).
    """
    ser = serial_utils.create_serial_connection(port, baudrate=baudrate)

    registers = []

    if address and read_all:
        raise click.UsageError("Options --address and -A can not be used together.")

    if cnc:
        if not address and not read_all:
            raise click.UsageError("--cnc requires --address or -A to be provided.")

        if read_all:
            for i in range(CNC_REG_SIZE):
                result = daq.cnc_read(i, ser)
                registers.append(result)
        elif address:
            result = daq.cnc_read(address, ser)
            registers.append(result)

        return registers

    if dm:
        if not address and not read_all:
            raise click.UsageError("--dm requires --address or -A to be provided")

        if read_all:
            for i in range(DM_REG_SIZE):
                result = daq.dm_read(i, ser)
                registers.append(result)
        elif address:
            result = daq.dm_read(address, ser)
            registers.append(result)

        return registers

    if read_all:
        for i in range(CNC_REG_SIZE):
            result = daq.cnc_read(i, ser)
            registers.append(result)

        for i in range(DM_REG_SIZE):
            result = daq.dm_read(i, ser)
            registers.append(result)

        return registers

    # should never get to this point
    return [(False, 0)]

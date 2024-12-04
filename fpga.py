import click
from utils import serial_utils, daq
from constants import CNC_BASE_ADD, CNC_REG_SIZE, DM_BASE_ADD, DM_REG_SIZE


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
@click.option("--all", "-A", "read_all", is_flag=True, help="Read all the registers")
def fpga_read(
    port: str, address: int, baudrate: int, read_all: bool
) -> list[tuple[bool, int]]:
    """
    Reads data from the FPGA at the specified address.

    Parameters:
        port (str): The name of the port (e.g., 'COM3' for Windows or '/dev/ttyUSB0' for Linux).
        address (int): The address of the register to read in decimal base.
        read_all (bool): Flag that defines if All register will be read.

    Returns:
        Tuple[bool, int]: A tuple where the first element indicates success (True/False),
                          and the second is the data read from the DAQ (32-bit unsigned).
    """
    ser = serial_utils.create_serial_connection(port, baudrate=baudrate)

    if read_all:
        registers = []

        for i in range(CNC_REG_SIZE):
            result = daq.daq_read(
                i + CNC_BASE_ADD, ser
            )  # TODO: Somar zero aqui faz sentido?
            registers.append(result)

        for i in range(DM_REG_SIZE):
            result = daq.daq_read(i + DM_BASE_ADD, ser)
            registers.append(result)

        print("------------------CNC REGISTER------------------")
        for address, data in registers[:CNC_REG_SIZE]:  # atualmente address = true
            print(f"Read: addr 0x{address} data 0x{data:08X}")

        print("------------------DM REGISTER------------------")
        for address, data in registers[16:]:
            print(f"Read: addr 0x{address} data 0x{data:08X}")

        return registers

    return list((daq.daq_read(address, ser),))

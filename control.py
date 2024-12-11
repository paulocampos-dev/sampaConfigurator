import click

from constants import CNTRL_REG_ADDR
from utils import serial_utils
from utils.daq import daq_read, dm_write


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
    "--serials",
    type=int,
    help="Define wich serial port will be used. The value accepted is in binary form."
    "The most signifcant value is associated with the 10th serial port and the least significant with 0th serial port."
    "The default value is 00000001111",
    default=0b00000001111,
)
@click.option(
    "--all", "-A", "select_all", is_flag=True, help="Select all the serial ports"
)
def serial_out(port: str, baudrate: int, serials: int, select_all: bool) -> bool:
    ser = serial_utils.create_serial_connection(port, baudrate)

    binary = bin(serials)[2:]
    register_list = [bit for bit in binary]

    if select_all:
        register_list = [1] * 11

    dm_write(CNTRL_REG_ADDR, int("".join(map(str, register_list))), ser)
    return True


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
    "--packets",
    "num_packets",
    default=1,
    show_default=True,
    help="Number orf packets +1 to acquire per enabled serial link (0 = infinite)",
)
def acquire(num_packets: int, port, baudrate) -> bool:
    ser = serial_utils.create_serial_connection(port, baudrate)

    control_reg_addr = daq_read(CNTRL_REG_ADDR, ser)[1]

    aux = (control_reg_addr & 0x0000FFFF) | (num_packets << 16)

    dm_write(CNTRL_REG_ADDR, aux | 1 << 12, ser)

    return True

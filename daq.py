import click
import utils.utils as utils
from constants import CMD_READ, CNC_BASE_ADD

"""
DAQ is for Data Aquisition
Here we define the two most important methods:
daq_read
daq_write
"""


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
    required=True,
    type=click.IntRange(0, 0xFFFF),
    help="16-bit register address to read from",
)
def daq_read(port: str, address: int, baudrate: int) -> tuple[bool, int]:
    """
    Reads data from the DAQ board at the specified address.

    Parameters:
        port (str): The name of the port (e.g., 'COM3' for Windows or '/dev/ttyUSB0' for Linux).
        address (int): The address of the register to read (16-bit unsigned).

    Returns:
        Tuple[bool, int]: A tuple where the first element indicates success (True/False),
                          and the second is the data read from the DAQ (32-bit unsigned).
    """

    address += int(CNC_BASE_ADD)
    ser = utils.create_serial_connection(port, baudrate=baudrate)
    try:
        # Ensure the serial port is open
        if not ser.is_open:
            click.echo("Error: Serial Port not open")
            return False, 0

        # Prepare command
        buf_s = bytearray(3)
        buf_s[0] = CMD_READ
        buf_s[1] = (address >> 8) & 0xFF  # High byte of address
        buf_s[2] = address & 0xFF  # Low byte of address

        try:
            ser.write(buf_s)
        except Exception as e:
            click.echo(f"Error writing data to the port {port} : {e}")
            return False, 0

        # Read response
        buf_r = bytearray(4)
        buf_r[0:3] = ser.read(4)

        # Convert buffer to a single 32-bit integer
        data = (buf_r[0] << 24) | (buf_r[1] << 16) | (buf_r[2] << 8) | buf_r[3]
        click.echo(f"Read: addr 0x{address:04X} data 0x{data:08X}")
        return True, data

    except Exception as ex:
        click.echo(f"Error reading from address {address} : {ex}")
        return False, 0

import click
import serial
from constants import CMD_READ, CNC_BASE_ADD, DM_BASE_ADD

"""
DAQ is for Data Aquisition
Here we define the two most important methods:
daq_read
daq_write
"""


def daq_read(address: int, ser: serial.Serial) -> tuple[bool, int]:
    """
    Reads data from the DAQ board at the specified address.

    Parameters:
        address (int): The address of the register to read (16-bit unsigned).
        ser (serial.Serial): The serial connection.

    Returns:
        Tuple[bool, int]: A tuple where the first element indicates success (True/False),
                          and the second is the data read from the DAQ (32-bit unsigned).
    """

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
            click.echo(f"Error writing data to the port {ser.port} : {e}")
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


def cnc_read(address: int, ser: serial.Serial) -> tuple[bool, int]:
    return daq_read(address + CNC_BASE_ADD, ser)


def dm_read(address: int, ser: serial.Serial) -> tuple[bool, int]:
    return daq_read(address + DM_BASE_ADD, ser)

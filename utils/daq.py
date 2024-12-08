import click
import serial
from constants import CMD_ACK, CMD_READ, CMD_WRITE, CNC_BASE_ADD, DM_BASE_ADD

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
            raise click.UsageError("Serial connection is not open")

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


def daq_write(address: int, data: int, ser: serial.Serial) -> bool:
    """
    Writes data to the DAQ board at the specified address.

    Parameters:
        address (int): The address of the register to read (16-bit unsigned).
        data (int): The data to be written.
        ser (serial.Serial): The serial connection.

    Returns:
        bool: Indicates wheter or not the operation was successfull.
    """
    try:
        # Ensure the serial port is open
        if not ser.is_open:
            raise click.UsageError("Serial connection is not open")

        # Prepare command
        buf_s = bytearray(7)
        buf_s[0] = CMD_WRITE | CMD_ACK
        buf_s[1] = (address >> 8) & 0xFF
        buf_s[2] = address & 0xFF
        buf_s[3] = (data >> 24) & 0xFF
        buf_s[4] = (data >> 16) & 0xFF
        buf_s[5] = (data >> 8) & 0xFF
        buf_s[6] = data & 0xFF  # LSB of data

        try:
            ser.write(buf_s)
        except Exception as e:
            click.echo(f"Error writing data to the address {address} : {e}")
            return False

        # Read the acknowledgment byte
        buf_r = ser.read()
        if len(buf_r) != 1:
            print("Failed to receive acknowledgment byte.")
            return False

        # Validate the acknowledgment byte
        if buf_r[0] != 0x5A:
            print(f"ACK: got 0x{buf_r[0]:02X} but should be 0x5A")
            return False

        # If everything is successful
        return True

    except Exception as ex:
        click.echo(f"Error writing to address {address} : {ex}")
        return False


def cnc_write(address: int, data: int, ser: serial.Serial) -> bool:
    return daq_write(address + CNC_BASE_ADD, data, ser)


def dm_write(address: int, data: int, ser: serial.Serial) -> bool:
    return daq_write(address + DM_BASE_ADD, data, ser)

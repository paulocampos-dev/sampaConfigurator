import serial


def create_serial_connection(
    port,
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=None,
) -> serial.Serial:
    """
    Creates and returns a serial connection.

    Parameters:
    - port: str - The name of the port (e.g., 'COM3' for Windows or '/dev/ttyUSB0' for Linux).
    - baudrate: int - The communication speed (default is 115200).
    - bytesize: int - Number of data bits (default is 8).
    - parity: int - Parity check (default is no parity).
    - stopbits: int - Number of stop bits (default is 1).
    - timeout: float or None - Read timeout in seconds (default is None).

    Returns:
    - serial.Serial object if successful, otherwise raises an exception.
    """
    try:
        ser = serial.Serial(
            port,
            baudrate,
            bytesize=bytesize,
            parity=parity,
            stopbits=stopbits,
            timeout=timeout,
        )
        return ser

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        raise

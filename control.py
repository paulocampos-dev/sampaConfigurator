import click


@click.command()
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
def serial_out(serials: int, select_all: bool) -> bool:
    binary = bin(serials)[2:]
    register_list = [bit for bit in binary]

    if select_all:
        register_list = [1] * 11

    print(register_list)
    # TODO: Fazer o resto da função né
    return True

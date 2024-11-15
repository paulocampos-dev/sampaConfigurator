import click


@click.command()
@click.argument("register")
@click.option("--version", help="versão né pai", default=1)
def getregx(register: str, version: int) -> None:
    click.echo(f"Você escolheu o registrador: {register}.")
    click.echo(f"A versão do código que você está usando é : {version}.")

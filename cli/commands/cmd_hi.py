import click


@click.command()
@click.argument('name')
def cli(name):
    """
    Greets the NAME.

    :param name: The person to greet
    """
    click.echo('Hi {0}'.format(name))

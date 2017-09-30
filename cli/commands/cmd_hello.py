import click


@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def cli(name):
    """
    Greets the NAME.

    :param name: User inputs a name
    :return: None
    """
    click.echo('Hello {0}'.format(name))

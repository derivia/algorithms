import click
import importlib


@click.command()
@click.option("--algorithm", prompt="Algorithm", help="The algorithm to run.")
def run(algorithm):
    try:
        module = importlib.import_module(f".impl.{algorithm}", package="src")
        if hasattr(module, "run"):
            module.run()
        else:
            raise NotImplementedError
    except NotImplementedError:
        exit(f"Error: {algorithm} not implemented.")

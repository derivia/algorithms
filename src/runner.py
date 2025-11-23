import importlib
import inspect
import click
from typing import get_origin, get_args


@click.command()
@click.option("--algorithm", prompt="Algorithm", help="The algorithm to run.")
def run(algorithm):
    try:
        module = importlib.import_module(f".impl.{algorithm}", package="src")

        if not hasattr(module, "run"):
            raise NotImplementedError

        run_fn = module.run
        sig = inspect.signature(run_fn)
        params = sig.parameters

        if len(params) == 0:
            return run_fn()

        click.echo(f"{algorithm}.run expects arguments:")
        kwargs = {}

        for name, param in params.items():
            annotation = param.annotation
            default = param.default if param.default is not inspect._empty else None
            label = name + (f" (default: {default})" if default is not None else "")

            raw_value = click.prompt(label, default=default)

            if annotation is not inspect._empty:
                origin = get_origin(annotation)

                if origin is list:
                    elem_type = get_args(annotation)[0]

                    if raw_value == default:
                        parsed = default
                    else:
                        try:
                            items = raw_value.split()
                            parsed = [elem_type(x) for x in items]
                        except Exception:
                            raise click.ClickException(
                                f"Invalid input for {name}. Use space-separated values, e.g.: 1 2 3 4"
                            )
                    raw_value = parsed

                else:
                    try:
                        raw_value = annotation(raw_value)
                    except Exception:
                        pass

            kwargs[name] = raw_value

        return run_fn(**kwargs)

    except NotImplementedError:
        exit(f"Error: {algorithm} not implemented.")

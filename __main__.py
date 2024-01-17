import argparse
import sys
from typing import Any

import yaml
from pathlib import Path
from core.utils import ExitCode
from containers import ApplicationContainer

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'
__version__ = '1.0.0'


def load_yaml_configuration() -> dict:
    def run_func(loader, node):
        value = loader.construct_scalar(node)
        if '.' in value:
            module_name, fun_name = value.rsplit('.', 1)
        else:
            module_name = '__main__'
            fun_name = value

        try:
            __import__(module_name)
        except ImportError as exc:
            raise

        module = sys.modules[module_name]
        fun = getattr(module, fun_name)

        try:
            return fun()
        except TypeError:
            return fun

    yaml.add_constructor('!func', run_func)

    with open(Path(Path(__file__).resolve().parent / 'config.yml'), 'r') as stream:
        return yaml.full_load(stream)


def set_debug_mode(handlers: dict[Any, Any]) -> dict[Any, Any]:
    for item in handlers:
        item.update({'level': 'DEBUG', 'format': '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> ' + item['format']})

    return handlers


def create_parser() -> argparse.ArgumentParser:
    _parser = argparse.ArgumentParser(
        prog="Nod32Scraper",
        description=f"Nod32Scraper - command-line tool for searching license key for ESET Nod"
    )

    _parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"Nod32Scraper version [{__version__}]"
    )

    _parser.add_argument(
        "--debug",
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction
    )

    return _parser


def run_container(params: dict[str, Any] = {}):
    container = ApplicationContainer()
    configuration = load_yaml_configuration()
    debug = params.pop("debug", False)

    if debug:
        configuration['log']['handlers'] = set_debug_mode(configuration['log']['handlers'])

    container.configuration.from_dict(configuration)
    container.init_resources()
    container.wire(modules=[sys.modules[__name__]])

    # main(**{k.lower(): v for k, v in params.items()})


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    if len(sys.argv) >= 2:
        pass
    else:
        parser.print_usage()
        sys.exit(ExitCode.USAGE)

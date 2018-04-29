#!/usr/bin/env python
import argparse
import logging
import os

from brigade.core import InitBrigade
from brigade.plugins.functions.text import print_result
from brigade.plugins.tasks.networking import napalm_get


def main(config, getters, debug):
    brg = InitBrigade(
        config_file=config,
        dry_run=False,
        num_workers=1 if debug else 20,
    )
    result = brg.run(
        name="Retrieving facts from the device",
        task=napalm_get,
        getters=getters,
    )
    print_result(
        result,
        severity_level=logging.DEBUG if debug else logging.INFO,
    )
    return result


def run():
    parser = argparse.ArgumentParser(
        description="Tool to backup network equipment using napalm"
    )
    parser.add_argument(
        "-d", "--debug", default=False, action="store_true"
    )
    parser.add_argument(
        "-c",
        "--config",
        default=os.environ.get(
            "BRIGADE_CONFIGURATION", "brigade.yaml"
        ),
        help="Path to brigade configuration. Defaults to brigade.yaml. "
        "Can be set via env variable BRIGADE_CONFIGURATION",
    )
    parser.add_argument(
        "-g",
        "--getter",
        default=[],
        action="append",
        help="Getters to retrieve. Pass this option as many times as you need",
    )
    args = parser.parse_args()
    main(args.config, args.getter, args.debug)


if __name__ == "__main__":
    run()

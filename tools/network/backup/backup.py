#!/usr/bin/env python
import argparse
import logging
import os

from nornir.core import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.files import write_file
from nornir.plugins.tasks.networking import napalm_get


def backup(task, path):
    r = task.run(
        task=napalm_get,
        getters=["config"],
        severity_level=logging.DEBUG,
    )
    task.run(
        task=write_file,
        filename=f"{path}/{task.host}",
        content=r.result["config"]["running"],
    )


def main(config, path, debug):
    nr = InitNornir(
        config_file=config,
        dry_run=False,
        num_workers=1 if debug else 20,
    )
    result = nr.run(
        name="Backup configuration of devices",
        task=backup,
        path=path,
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
            "BRIGADE_CONFIGURATION", "nornir.yaml"
        ),
        help="Path to nornir configuration. Defaults to nornir.yaml. "
        "Can be set via env variable BRIGADE_CONFIGURATION",
    )
    parser.add_argument(
        "-p",
        "--path",
        default="backups",
        help="Path to directory where to save the configuration backups. Defaults to './backups/'",
    )
    args = parser.parse_args()
    main(args.config, args.path, args.debug)


if __name__ == "__main__":
    run()

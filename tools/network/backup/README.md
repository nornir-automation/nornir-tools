backup
======

Tool that retrieves the running configuration from a device and stores it locally.

For help:

    $ tools/network/backup/backup.py --help
    usage: backup.py [-h] [-d] [-c CONFIG] [-p PATH]

    Tool to backup network equipment using napalm

    optional arguments:
      -h, --help            show this help message and exit
      -d, --debug
      -c CONFIG, --config CONFIG
                            Path to brigade configuration. Defaults to
                            brigade.yaml. Can be set via env variable
                            BRIGADE_CONFIGURATION
      -p PATH, --path PATH  Path to directory where to save the configuration
                            backups. Defaults to './backups/'

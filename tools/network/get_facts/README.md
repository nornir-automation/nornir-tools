get\_facts
==========

Tool that retrieves facts from devices

For help:

     $ ./tools/network/get_facts/get_facts.py --help
    usage: get_facts.py [-h] [-d] [-c CONFIG] [-g GETTER]

    Tool to backup network equipment using napalm

    optional arguments:
      -h, --help            show this help message and exit
      -d, --debug
      -c CONFIG, --config CONFIG
                            Path to nornir configuration. Defaults to
                            nornir.yaml. Can be set via env variable
                            BRIGADE_CONFIGURATION
      -g GETTER, --getter GETTER
                            Getters to retrieve. Pass this option as many times as
                            you need

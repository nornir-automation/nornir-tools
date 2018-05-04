#!/usr/bin/env python

from brigade.core import InitBrigade
from brigade.plugins.functions.text import print_result
from brigade.plugins.tasks.networking import napalm_get


# Initialize brigade
brg = InitBrigade(
    config_file="brigade.yaml", dry_run=True, num_workers=20
)

# Let's just filter the hosts we want to operate on
cmh = brg.filter(type="network_device", site="cmh")

# Let's retrieve the information and print them on screen
results = cmh.run(
    task=napalm_get, getters=["facts", "interfaces"]
)
print_result(results)

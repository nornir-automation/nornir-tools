#!/usr/bin/env python

from nornir.core import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_get


# Initialize nornir
nr = InitNornir(
    config_file="nornir.yaml", dry_run=True, num_workers=20
)

# Let's just filter the hosts we want to operate on
cmh = nr.filter(type="network_device", site="cmh")

# Let's retrieve the information and print them on screen
results = cmh.run(
    task=napalm_get, getters=["facts", "interfaces"]
)
print_result(results)

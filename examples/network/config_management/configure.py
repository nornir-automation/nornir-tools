#!/usr/bin/env python
"""
Runbook to configure datacenter
"""
from brigade.core import InitBrigade
from brigade.plugins.functions.text import (
    print_result, print_title
)
from brigade.plugins.tasks.data import load_yaml
from brigade.plugins.tasks.networking import napalm_configure
from brigade.plugins.tasks.text import template_file


def configure(task):
    """
    This function groups all the tasks needed to configure the
    network:

        1. Load extra data
        2. Use templates to build configuration
        3. Deploy configuration on the devices
    """
    r = task.run(
        name="Base Configuration",
        task=template_file,
        template="base.j2",
        path=f"templates/{task.host.nos}",
    )
    # r.result holds the result of rendering the template
    config = r.result

    r = task.run(
        name="Loading extra data",
        task=load_yaml,
        file=f"extra_data/{task.host}/l3.yaml",
    )
    # r.result holds the data contained in the yaml files
    # we load the data inside the host itself for further use
    task.host["l3"] = r.result

    r = task.run(
        name="Interfaces Configuration",
        task=template_file,
        template="interfaces.j2",
        path=f"templates/{task.host.nos}",
    )
    # we append the generated configuration
    config += r.result

    r = task.run(
        name="Routing Configuration",
        task=template_file,
        template="routing.j2",
        path=f"templates/{task.host.nos}",
    )
    config += r.result

    r = task.run(
        name="Role-specific Configuration",
        task=template_file,
        template=f"{task.host['role']}.j2",
        path=f"templates/{task.host.nos}",
    )
    # we update our hosts' config
    config += r.result

    task.run(
        name="Loading Configuration on the device",
        task=napalm_configure,
        replace=False,
        configuration=config,
    )


# Initialize brigade
brg = InitBrigade(
    config_file="brigade.yaml", dry_run=True, num_workers=20
)


# Let's just filter the hosts we want to operate on
cmh = brg.filter(type="network_device", site="cmh")

# Let's call the grouped tasks defined above
results = cmh.run(task=configure)

# Let's show everything on screen
print_title("Playbook to configure the network")
print_result(results)

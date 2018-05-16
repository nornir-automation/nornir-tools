import os
import shutil

import pytest


@pytest.fixture(scope="session", autouse=True)
def tmp_folder(request):
    tmp = "/tmp/nr_tools_test"

    def fin():
        shutil.rmtree(tmp)

    request.addfinalizer(fin)

    os.mkdir(tmp)
    return tmp

import os
import shutil

import pytest


@pytest.fixture(scope="session", autouse=True)
def tmp_folder(request):
    tmp = "/tmp/brg_tools_test"

    def fin():
        shutil.rmtree(tmp)

    request.addfinalizer(fin)

    os.mkdir(tmp)
    return tmp

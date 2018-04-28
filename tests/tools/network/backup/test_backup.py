import os

import backup

from tests.wrapper import wrap_cli_test


class TestBackup(object):

    @wrap_cli_test(output="tests/tools/network/backup/output", save_output=False)
    def test_backup(self, tmp_folder):
        folder = "{}/test_backup".format(tmp_folder)
        os.mkdir(folder)
        result = backup.main("tests/mocked/config.yaml", folder, False)
        assert len(result) == 8
        for host, results in result.items():
            assert not results.failed
            assert len(results) == 3

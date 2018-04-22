import backup

from tests.wrapper import wrap_cli_test


class TestBackup(object):

    @wrap_cli_test(output="tests/tools/network/backup/output")
    def test_backup(self):
        result = backup.main("tests/mocked/config.yaml", "/tmp", False)
        assert len(result) == 8
        for host, results in result.items():
            assert not results.failed
            assert len(results) == 3

from tests.wrapper import wrap_cli_test

from tools.network.get_facts import get_facts


class TestBackup(object):

    @wrap_cli_test(
        output="tests/tools/network/get_facts/output",
        save_output=False,
    )
    def test_get_facts(self, tmp_folder):
        result = get_facts.main(
            "tests/mocked/config.yaml",
            ["interfaces", "config"],
            False,
        )
        assert len(result) == 8
        for host, results in result.items():
            assert not results.failed
            assert len(results) == 1

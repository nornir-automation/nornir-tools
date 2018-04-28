import io
import os
import sys

from decorator import decorator


def wrap_cli_test(output, save_output=False):
    """
    This decorator captures the stdout and stder and compare it
    with the contacts of the specified files.

    Instead of save_output you can set the env variable BRG_TOOLS_TESTS_SAVE_OUTPUT

    Arguments:
        output (string): Path to the output. stdout and stderr prefixes will be added automatically
        save_output (bool): Whether to save the output or not. Useful when creating the tests
    """

    @decorator
    def run_test(func, *args, **kwargs):
        stdout = io.StringIO()
        backup_stdout = sys.stdout
        sys.stdout = stdout

        stderr = io.StringIO()
        backup_stderr = sys.stderr
        sys.stderr = stderr

        func(*args, **kwargs)
        sys.stdout = backup_stdout
        sys.stderr = backup_stderr

        if (
            save_output
            or os.getenv("BRG_TOOLS_TESTS_SAVE_OUTPUT")
        ):
            with open(f"{output}.stdout", "w+") as f:
                f.write(stdout.getvalue())
            with open(f"{output}.stderr", "w+") as f:
                f.write(stderr.getvalue())

        with open(f"{output}.stdout", "r") as f:
            expected = f.read()
            assert stdout.getvalue() == expected
        with open(f"{output}.stderr", "r") as f:
            expected = f.read()
            assert stderr.getvalue() == expected

    return run_test

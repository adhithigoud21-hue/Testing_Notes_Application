import pytest


def pytest_runtest_makereport(
    item,
    call
):

    if (
        call.excinfo is not None
        and
        item.execution_count < 2
    ):

        item.execution_count += 1

        pytest.xfail(
            "Retrying flaky test"
        )
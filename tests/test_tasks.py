from prefect import flow

from prefect_datafold.tasks import (
    goodbye_prefect_datafold,
    hello_prefect_datafold,
)


def test_hello_prefect_datafold():
    @flow
    def test_flow():
        return hello_prefect_datafold()

    result = test_flow()
    assert result == "Hello, prefect-datafold!"


def goodbye_hello_prefect_datafold():
    @flow
    def test_flow():
        return goodbye_prefect_datafold()

    result = test_flow()
    assert result == "Goodbye, prefect-datafold!"

import os

import pytest
from keyringrs import Entry

pytestmark = pytest.mark.skipif(
    os.environ.get("KEYRINGRS_RUN_INTEGRATION_TESTS") != "1",
    reason="requires a configured system keyring backend",
)


def test_entry():
    entry = Entry("my-service", "my-name")

    # Set a password
    pass_str = "0Xl$$K6o2bBwDe"
    entry.set_password(pass_str)

    # Retrieve the password
    assert entry.get_password() == pass_str

    # Delete the credential
    entry.delete_credential()

    with pytest.raises(KeyError):
        _ = entry.get_password()

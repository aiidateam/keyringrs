import platform
from keyringrs import CredentialType, Entry


def test_imports():
    assert Entry is not None
    assert isinstance(CredentialType.Default, CredentialType)
    if platform.system() == "linux":
        assert isinstance(CredentialType.KeyUtils, CredentialType)

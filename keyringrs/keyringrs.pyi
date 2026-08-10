from typing import ClassVar

class CredentialType:
    """Native Rust credential type exposed by the extension module."""

    Default: ClassVar["CredentialType"]
    KeyUtils: ClassVar["CredentialType"]

class Entry:
    """
    Represents a credential entry. This class encapsulates information about
    the service, user, optional target, and the type of credential. It also
    provides methods to set, get, and delete the associated password.
    """

    def __new__(
        cls,
        service: str,
        user: str,
        target: str | None = None,
        credential_type: CredentialType = CredentialType.Default,
    ) -> "Entry":
        """
        Construct a new Entry instance.

        :param service:
            The name of the service or system this credential is associated with.

        :param user:
            The username or identifier for which credentials are stored.

        :param target:
            An optional target or sub-identifier (e.g., a specific account or region).

        :param credential_type:
            The type of the credential, as defined in :class:`CredentialType`.
            Defaults to :attr:`CredentialType.Default`.

        :return:
            A new instance of this class.
        """
        ...

    def set_password(self, password: str) -> None:
        """
        Set the password for this credential entry.

        :param password:
            The password to store.
        """
        ...

    def get_password(self) -> str:
        """
        Retrieve the stored password.

        :return:
            The password associated with this credential entry.
        """
        ...

    def delete_credential(self) -> None:
        """
        Remove or invalidate the credential associated with this entry, so that
        it can no longer be retrieved.
        """
        ...

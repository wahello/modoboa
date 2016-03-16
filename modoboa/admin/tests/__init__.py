"""modoboa-admin unit tests."""

from .account import AccountTestCase, PermissionsTestCase
from .alias import AliasTestCase
from .api import DomainAPITestCase, AccountAPITestCase, AliasAPITestCase
from .domain import DomainTestCase
from .domain_alias import DomainAliasTestCase
from .export import ExportTestCase
from .import_ import ImportTestCase
from .mapfiles import MapFilesTestCase
from .password_schemes import PasswordSchemesTestCase
from .user import ForwardTestCase

__all__ = [
    'AccountAPITestCase',
    'AccountTestCase',
    'AliasAPITestCase',
    'AliasTestCase',
    'DomainAPITestCase',
    'DomainTestCase',
    'DomainAliasTestCase',
    'ExportTestCase',
    'ForwardTestCase',
    'ImportTestCase',
    'MapFilesTestCase',
    'PasswordSchemesTestCase',
    'PermissionsTestCase',
]
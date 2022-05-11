import typing as tp

from logging import getLogger

from account import Account
from custom_functions import CustomFunctions

logger = getLogger(__name__)


class BaseClass:
    """
    Base class for different modules to initialize `custom_functions` instance for further work.
    """

    def __init__(self, account: Account, rws_sub_owner: tp.Optional[str] = None):
        """
        Assign Account dataclass parameters and create an empty interface attribute for a decorator.

        :param account: Account dataclass with seed, websocket address and node type_registry.
        :param rws_sub_owner: Subscription owner address. If passed, all extrinsics will be executed via RWS
            subscriptions.

        """
        self.account: Account = account
        self.custom_functions: CustomFunctions = CustomFunctions(account, rws_sub_owner=rws_sub_owner)

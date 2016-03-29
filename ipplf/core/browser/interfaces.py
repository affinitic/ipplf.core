# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IIpplfCoreLayer(IDefaultBrowserLayer):
    """
    Layer for all IPPLF developments
    """


class IManageCommon(Interface):
    """
    IManageCommon
    """

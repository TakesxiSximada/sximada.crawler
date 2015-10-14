# -*- coding: utf-8 -*-
from zope.interface import implementer
from zope.component.interfaces import IFactory


@implementer(IFactory)
class EntryFactory(object):
    pass


@implementer(IFactory)
class TimelineFactory(object):
    pass

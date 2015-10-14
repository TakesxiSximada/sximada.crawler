# -*- coding: utf-8 -*-
from zope.interface import (
    Interface,
    Attribute,
    )


class IEntry(Interface):
    title = Attribute(u'')
    description = Attribute(u'')
    author = Attribute(u'')
    created_at = Attribute(u'')
    updated_at = Attribute(u'')
    deleted_at = Attribute(u'')


class ITimeline(Interface):
    entries = Attribute(u'')

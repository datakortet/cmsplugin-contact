# -*- coding: utf-8 -*-

"""Test that all modules are importable.
"""

import cmsplugin_contact
import cmsplugin_contact.admin
import cmsplugin_contact.models
import cmsplugin_contact.forms
import cmsplugin_contact.utils
import cmsplugin_contact.cms_plugins
import cmsplugin_contact.middleware
import cmsplugin_contact.migrations
import cmsplugin_contact.nospam
import cmsplugin_contact.nospam.forms
import cmsplugin_contact.nospam.utils
import cmsplugin_contact.nospam.fields
import cmsplugin_contact.nospam.widgets
import cmsplugin_contact.settings


def test_import_cmsplugincontact():
    """Test that all modules are importable.
    """
    
    assert cmsplugin_contact
    assert cmsplugin_contact.admin
    assert cmsplugin_contact.models
    assert cmsplugin_contact.forms
    assert cmsplugin_contact.utils
    assert cmsplugin_contact.cms_plugins
    assert cmsplugin_contact.middleware
    assert cmsplugin_contact.migrations
    assert cmsplugin_contact.nospam
    assert cmsplugin_contact.nospam.forms
    assert cmsplugin_contact.nospam.utils
    assert cmsplugin_contact.nospam.fields
    assert cmsplugin_contact.nospam.widgets
    assert cmsplugin_contact.settings
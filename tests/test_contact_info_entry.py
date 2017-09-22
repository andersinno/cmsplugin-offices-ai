# -*- coding: utf-8 -*-
import pytest

from cmsplugin_offices_ai.models.information_entries import ContactInformationEntry, EntryType


@pytest.mark.django_db
def test_contact_info_entry_href_prefix():
    entry_1 = ContactInformationEntry(entry_type=EntryType.EMAIL, value="test@example.com")
    entry_2 = ContactInformationEntry(entry_type=EntryType.PHONE, value="0400123456")
    entry_3 = ContactInformationEntry(entry_type=EntryType.FAX, value="123456789")
    assert entry_1.get_link_href_prefix() == "mailto:"
    assert entry_2.get_link_href_prefix() == "tel:"
    assert entry_3.get_link_href_prefix() == "fax:"

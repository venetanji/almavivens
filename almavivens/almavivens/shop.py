# -*- coding: utf-8 -*-
# Copyright (c) 2017, Gio and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

@frappe.whitelist(allow_guest=True)
def get_shops_list():
	return frappe.get_all("Shop", fields=["shop_name", "address", "lat", "lon"])

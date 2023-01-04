# Copyright (c) 2023, John Rech Cabatana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import pandas

class SOBulkSearch(Document):
	pass

@frappe.whitelist()
def read_file(location):
	org = frappe.get_site_path()
	excel_data_df = pandas.read_excel(org+location)
	list_so = excel_data_df['SalesOrder'].tolist()
	data = [["name","in",list_so]]
	return data
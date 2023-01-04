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
	#print(frappe.get_site_path()+location)
	list_so = excel_data_df['SalesOrder'].tolist()
	#[["name","=","SAL-ORD-2021-100-008"],["name","=","SAL-ORD-2021-100-009"]]
	
	data = [["name","in",list_so]]
	return data
# Copyright (c) 2024, Deepak and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DSCPurchaseOrder(Document):
	def validate(self):
		if self.workflow_state:
			self.previous_state = self.workflow_state

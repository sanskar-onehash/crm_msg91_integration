# Copyright (c) 2025, OneHash and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from crm_msg91_integration.msg91.integration import service as msg91


class MSG91Settings(Document):

    def send_otp(self, *args, **kwargs):
        msg91.send_otp(*args, **kwargs)

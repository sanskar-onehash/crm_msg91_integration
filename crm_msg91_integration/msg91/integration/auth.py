import frappe


def get_auth_key():
    msg91_settings = frappe.get_single("MSG91 Settings")

    if not msg91_settings.enabled:
        frappe.throw("MSG91 is not enabled.")

    return msg91_settings.get_password("auth_key")

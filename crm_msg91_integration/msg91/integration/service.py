import frappe
from crm_msg91_integration.msg91.integration import api, utils


def send_otp(otp=None, mobile_no=None, expiry=None, template_params=None):
    msg91_settings = frappe.get_single("MSG91 Settings")
    if not msg91_settings.enabled:
        frappe.throw("MSG91 Integration is not enabled")
    if not msg91_settings.otp_template:
        frappe.throw("OTP Template is missing in MSG91 Settings")

    otp_res = api.send_otp(
        otp,
        mobile_no,
        expiry or utils.OTP_EXPIRY,
        msg91_settings.otp_template,
        template_params,
        raise_exception=False,
    )
    otp_data = utils.parse_otp_res(otp_res)

    if otp_data.get("type") == "success":
        return otp_data

    frappe.throw(f"Error sending otp: {otp_data.get('message')}")


def verify_otp(otp, mobile_no):
    msg91_settings = frappe.get_single("MSG91 Settings")
    if not msg91_settings.enabled:
        frappe.throw("MSG91 Integration is not enabled")

    otp_res = api.verify_otp(
        otp,
        mobile_no,
        raise_exception=False,
    )
    otp_data = utils.parse_otp_res(otp_res)

    if otp_data.get("type") == "success":
        return otp_data

    frappe.throw(f"Error sending otp: {otp_data.get('message')}")

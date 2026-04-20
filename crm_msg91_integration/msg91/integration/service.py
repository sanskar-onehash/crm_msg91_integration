import frappe
from crm_msg91_integration.msg91.integration import api, utils


def send_otp(otp=None, mobile_no=None, expiry=None, template_params=None):
    msg91_settings = frappe.get_single("MSG91 Settings")
    if not msg91_settings.enabled:
        frappe.throw("MSG91 Integration is not enabled")
    if not msg91_settings.otp_template:
        frappe.throw("OTP Template is missing in MSG91 Settings")

    expiry = expiry or utils.OTP_EXPIRY
    otp_res = api.send_otp(
        otp,
        mobile_no,
        expiry,
        msg91_settings.otp_template,
        template_params,
        raise_exception=False,
    )
    otp_data = utils.parse_otp_res(otp_res)
    message_sent = otp_data.get("type") == "success"

    try:
        frappe.get_doc(
            {
                "doctype": "MSG91 OTP Log",
                "mobile_no": mobile_no,
                "otp": otp,
                "expiry": expiry,
                "status": "Success" if message_sent else "Failed",
                "response": frappe.json.dumps(otp_data),
                "template_params": frappe.json.dumps(template_params),
            }
        ).insert(ignore_permissions=True)
    except Exception:
        pass

    if message_sent:
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

    return {"status": otp_data.get("type"), "message": otp_data.get("message")}

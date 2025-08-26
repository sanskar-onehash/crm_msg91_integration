from crm_msg91_integration.msg91.integration import utils


def send_otp(
    otp, mobile, otp_expiry, template_id, template_values, raise_exception=True
):
    params = {
        "otp": otp,
        "mobile": mobile,
        "otp_expiry": otp_expiry,
        "template_id": template_id,
    }

    return utils.make_post_request(
        "/otp", params=params, data=template_values, raise_exception=raise_exception
    )


def verify_otp(otp, mobile, raise_exception=True):
    params = {
        "otp": otp,
        "mobile": mobile,
    }

    return utils.make_get_request(
        "/otp/verify", params=params, raise_exception=raise_exception
    )

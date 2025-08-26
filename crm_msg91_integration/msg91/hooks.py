from crm_msg91_integration.msg91.integration import service


def send_otp(*args, **kwargs):
    return service.send_otp(*args, **kwargs)


def verify_otp(*args, **kwargs):
    return service.verify_otp(*args, **kwargs)

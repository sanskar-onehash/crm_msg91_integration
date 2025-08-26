import requests
from crm_msg91_integration.msg91.integration import auth

API_VERSION = "v5"
BASE_URI = f"https://control.msg91.com/api/{API_VERSION}"
OTP_EXPIRY = "3"  # minutes


def prepare_headers():
    return {"Content-Type": "application/JSON", "content-type": "application/json"}


def prepare_params(params, authenticate):
    if not params:
        params = {}
    elif "authkey" in params:
        return params

    if authenticate:
        params["authkey"] = auth.get_auth_key()

    return params


def make_get_request(endpoint, params=None, authenticate=True, raise_exception=True):
    headers = prepare_headers()
    params = prepare_params(params, authenticate)

    res = requests.get(f"{BASE_URI}{endpoint}", headers=headers, params=params)

    if raise_exception:
        res.raise_for_status()

    return res


def make_post_request(
    endpoint, params=None, data=None, json=None, authenticate=True, raise_exception=True
):
    headers = prepare_headers()
    params = prepare_params(params, authenticate)

    res = requests.post(
        f"{BASE_URI}{endpoint}", headers=headers, params=params, data=data, json=json
    )

    if raise_exception:
        res.raise_for_status()

    return res


def make_put_request(
    endpoint, params=None, data=None, json=None, authenticate=True, raise_exception=True
):
    headers = prepare_headers()
    params = prepare_params(params, authenticate)

    res = requests.put(
        f"{BASE_URI}{endpoint}", headers=headers, params=params, data=data, json=json
    )

    if raise_exception:
        res.raise_for_status()

    return res


def make_delete_request(
    endpoint, params=None, data=None, json=None, authenticate=True, raise_exception=True
):
    headers = prepare_headers()
    params = prepare_params(params, authenticate)

    res = requests.delete(
        f"{BASE_URI}{endpoint}", headers=headers, params=params, data=data, json=json
    )

    if raise_exception:
        res.raise_for_status()

    return res


def parse_otp_res(otp_res):
    return otp_res.json()

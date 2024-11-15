from django.conf import settings


def env_setting(key, default=None):
    import os
    return os.environ.get(key, default)


if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

MERCHANT = env_setting('MERCHANT')

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"
phone = 'YOUR_PHONE_NUMBER'
# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/baraato/payment/verify/'

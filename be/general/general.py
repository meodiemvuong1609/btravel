import random
from django.core.mail import send_mail
from django.template.loader import render_to_string
import requests
import base64

status_response = {
    '200': 'Ok Request',
    '400': "Bad Request"
}

def lookup_card(bin, accountNumber, transferType):
    # Set up the authentication credentials
    username = 'customer-0968262995-user07'
    password = 'Y3VzdG9tZXItMDk2ODI2Mjk5NS11c2VyMDc='

    # Encode the credentials
    credentials = f'{username}:{password}'
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    # Make a GET request to a protected resource
    url = 'https://api.vietqr.org/vqr/api/token_generate'
    headers = {
        'Authorization': f'Basic {encoded_credentials}'
    }
    response = requests.post(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        return 400, "Authentication VIETQR failed"
    access_token = response_data["access_token"]

    url_lookup = "http://api.vietqr.org/vqr/bank/api/account/info"

    response_lookup = requests.get(url_lookup, headers={"Authorization": f"Bearer {access_token}"}, params={"bin": bin, "accountNumber": accountNumber, "transferType": transferType, "accountType": "ACCOUNT"})
    if response_lookup.status_code != 200:
        return 400, "Lookup card failed"
    response_lookup_data = response_lookup.json()
    ERROR_MESSAGE = {
        "E05": "Lỗi hệ thống",
        "E32": "Không tìm thấy tên người dùng",
        "E33": "Params khoong hợp lệ",
    }
    if "status" in response_lookup_data:
        return 400, ERROR_MESSAGE[response_lookup_data["status"]]
    if "accountName" in response_lookup_data:
        return 200, response_lookup_data["accountName"]
    return 400, "Server error"


def convert_response(message, status_code, data=None, count=None):
    """
        We want to convert body response to normalization.
    """
    
    response = {
        "message": message,
        "code": status_code,
    }
    
    if data is not None:
        response.update({"data": data})
    if count is not None:
        response.update({"count": count})
        
    return response
        
def generate_qr_code(payload):
     # Set up the authentication credentials
    username = 'customer-0968262995-user07'
    password = 'Y3VzdG9tZXItMDk2ODI2Mjk5NS11c2VyMDc='

    # Encode the credentials
    credentials = f'{username}:{password}'
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    # Make a GET request to a protected resource
    url = 'https://api.vietqr.org/vqr/api/token_generate'
    headers = {
        'Authorization': f'Basic {encoded_credentials}'
    }
    response = requests.post(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        return 400, "Authentication VIETQR failed"
    access_token = response_data["access_token"]

    url_generate = "https://api.vietqr.org/vqr/api/qr/generate-customer"
    response_generate = requests.post(url_generate, headers={"Authorization": f"Bearer {access_token}"}, json=payload)
    if response_generate.status_code != 200:
        return 400, "Generate QR code failed"
    response_generate_data = response_generate.json()
    ERROR_MESSAGE = {
        "E05": "Lỗi hệ thống",
        "E24": "Không tìm thấy ngân hàng tương ứng với bankCode (mã ngân hàng)",
        "E26": "Nội dung không hợp lệ (dài hơn 50 ký tự)",
    }
    if "status" in response_generate_data:
        return 400, ERROR_MESSAGE[response_generate_data["status"]]
    if "qrCode" in response_generate_data:
        return 200, response_generate_data
    return 400, "Server error"

#random otp 
def random_otp(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return random.randint(range_start, range_end)

#send otp
def send_otp(email=[], template=None):
    if template == None:
        return None
    otp = random_otp(6)
    html_mail = render_to_string(template, context={"otp": otp})
    send = send_mail("", "", "mykiot2023@gmail.com", [email], fail_silently=False, html_message=html_mail)   
    return otp

def Paginate(data, query_params, page=1, limit=20):
    page = int(query_params.get("page", page))
    limit = int(query_params.get("limit", limit))
    start = (page - 1) * limit
    end = page * limit
    return data[start:end]

def send_order_mail(email, template, context):
    html_mail = render_to_string(template, context=context)
    subject = "Bạn có một đơn hàng mới từ Mykiot"
    send = send_mail(subject, "", "mykiot2023@gmail.com", [email], fail_silently=False, html_message=html_mail)
    return send

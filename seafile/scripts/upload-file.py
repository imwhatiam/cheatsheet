# -*- coding: utf-8 -*-

import requests
import email.utils

# get upload url
url = "https://demo.seafile.top/api2/repos/44f59baf-4686-49c7-8169-006311bc8d34/upload-link/"
headers = {"Authorization": "Token e86bd23e0e398b50839c639055823aa9d6315bc5"}
params = {'p': '/'}
resp = requests.get(url, params=params, headers=headers)
upload_url = resp.json()

# upload file
file_name = '中文.txt'
files = {
    'file': (file_name, open(file_name, 'rb')),
    'parent_dir': '/',
}

print(files)

try:
    file_name.encode('ascii')
except UnicodeEncodeError:

    def rewrite_request(prepared_request):

        old_content = 'filename*=' + email.utils.encode_rfc2231(file_name, 'utf-8')
        old_content = old_content.encode()

        new_content = 'filename="{}"'.format(file_name)
        new_content = new_content.encode()

        prepared_request.body = prepared_request.body.replace(old_content, new_content)

        return prepared_request

    resp = requests.post(upload_url, files=files, auth=rewrite_request)
else:
    resp = requests.post(upload_url, files=files)

print(resp.content)

import os
import time
import json
import requests
import datetime

dtable_web_log = '/opt/seatable/shared/nginx-logs/dtable-web.error.log'
dtable_server_log = '/opt/seatable/shared/seatable/logs/dtable-server.log'

dtable_web_error_log_mtime = os.path.getmtime(dtable_web_log)
dtable_server_error_log_mtime = os.path.getmtime(dtable_server_log)
current_timestamp = time.time()

send_dtable_web_msg = False
send_dtable_server_msg = False

if current_timestamp - dtable_web_error_log_mtime < 60:
    send_dtable_web_msg = True
    with open(dtable_web_log) as f:
        all_lines = f.readlines()
        all_lines_without_wopi = []
        for line in all_lines:
            if 'wopi' in line.lower():
                continue
            if '[info]' in line.lower():
                continue
            else:
                all_lines_without_wopi.append(line)
        dtable_web_content = all_lines_without_wopi[-1]

if current_timestamp - dtable_server_error_log_mtime < 60:
    with open(dtable_server_log) as f:
        all_lines = f.readlines()
        all_lines_without_wopi = []
        for line in all_lines:
            if '[error]' not in line.lower():
                continue
            else:
                all_lines_without_wopi.append(line)

        last_error_msg = all_lines_without_wopi[-1]
        error_time_str = last_error_msg[1:20]
        error_datetime = datetime.datetime.strptime(error_time_str, "%Y-%m-%dT%H:%M:%S")
        error_timestamp = int(time.mktime(error_datetime.timetuple()))

        if current_timestamp - error_timestamp <= 5 * 60:
            dtable_server_content = all_lines_without_wopi[-1]
            send_dtable_server_msg = True

corpid = 'corp id'
corpsecret = 'app secret'
get_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (corpid, corpsecret)
resp = requests.get(get_url)
access_token = resp.json()['access_token']

# 在应用的可见范围内，添加此部门，
data = {
    "toparty": 18,  # Weixin department: nginx-dtable_web-dtable_server-error
    "msgtype": "text",
    "agentid": 1000064,  # Weixin agent: nginx-dtable_web-dtable_server-error
    "safe": 0
}
post_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % access_token

if send_dtable_web_msg:
    data['text'] = {"content": 'dtable-web: ' + dtable_web_content}
    resp = requests.post(post_url, data=json.dumps(data))

if send_dtable_server_msg:
    data['text'] = {"content": 'dtable-server: ' + dtable_server_content}
    requests.post(post_url, data=json.dumps(data))

# -*- coding: utf-8 -*-
import jenkins # pip install python-jenkins
import json
import requests # pip install requests
import sys
 
reload(sys)
sys.setdefaultencoding('utf-8')
 
server_url = '' # ex) http://jenkinskorea.jenkins.org
user = '' # ex) admin
passwd = '' # ex) admin
 
server = jenkins.Jenkins(server_url, username=user, password=passwd)
 
# get console output
job_name = 'check_appannie'
build_num = 128
console_output = server.get_build_console_output(job_name, build_num)
 
print ('*' * 200)
print (console_output)
print ('*' * 200)
 
# send to slack...
slack_url = '' # ex) https://hooks.slack.com/services/T75QJS2AC/BAHLN2P8R/o5Q3IsOE8q7le123456789
slack_payload = {"text" : str(console_output)}
res = requests.post(url=slack_url, data=json.dumps(slack_payload))
print (res)
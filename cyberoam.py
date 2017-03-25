#!/usr/bin/python
import requests
import sys

username = "USERNAME_GOES_HERE"
password = "PLAINTEXT_PASSWORD_GOES_HERE"
gateway = "CYBEROAM_GATEWAY_GOES_HERE"
global url
url = "http://{}:8090/httpclient.html".format(gateway)


def login():
    global url, username, password
    try:
        data_login = {'mode': 191, 'username': username, 'password': password, 'btnSubmit': 'Login'}
        r = s.post(url, data=data_login)
    except Exception:
        print "Error during login. Make sure your username and password is correct."
    else:
        print "Logged In."


def logout():
    global url, username, password
    try:
        data = {'mode': 193, 'username': username, 'password': password, 'btnSubmit': 'Logout'}
        s.post(url, data=data)
    except Exception:
        print "Error during logout. Logout via webclient."
    else:
        print "Logged Out."
        sys.exit()


with requests.Session() as s:
        login()
        inp = raw_input("Press 'Enter' to logout.")
        if inp:
            logout()
#v.10 no multithreading in this version

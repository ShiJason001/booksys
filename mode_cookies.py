from flask import make_response, request

def set_cookies(name, msg):
    resp = make_response("success")
    resp.set_cookie(name, msg, max_age=3600)
    return resp

def get_cookies(name):
    cookie_1 = request.cookies.get(name)
    return cookie_1

def delete_cookies(name):
    resp = make_response("delete success")
    resp.delete_cookie(name)
    return resp

from flask import make_response, jsonify

SUCCESS = {
    "code": 20000,
    "data": "success"
}

NOTFOUND = {
    "code": 20000,
    "data": "not found"
}

AUTHFAILED = {
    "code": 20000,
    "data": "auth failed"
}

EXPIRED = {
    "code": 50012,
    "data": "token is expired"
}

FORBIDDEN = {
    "code": 20000,
    "data": "forbidden, not in scope"
}


def response_data(response):
    return make_response(jsonify(response))

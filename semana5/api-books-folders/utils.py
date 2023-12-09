from flask import jsonify


def response(ok, data, status):
    return (
        jsonify(
            {
                "ok": ok,
                "data": data,
            }
        ),
        status,
    )


def response_success(data, status=200):
    return response(True, data, status)


def response_error(data, status=500):
    return response(False, data, status)


def generate_id(data):
    return len(data) + 1

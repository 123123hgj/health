from flask import jsonify


def success(message=''):
    return jsonify({'code': 200, 'message': message})


def param_error(message):
    return jsonify({'code': 400, 'message': message})

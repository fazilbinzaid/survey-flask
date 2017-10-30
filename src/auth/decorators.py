from functools import wraps

from flask import request, Response


def check_auth(username, password):
    """
    Function to check valid username / password.
    Now hardcoding the username and password for simple purposes.
    """
    return username == "admin" and password == "testflask1234"

def unauthenticate():
    """
    Returns 401 Response that enables basic auth.
    """
    return Response(
        '''Could not verify your access level for that URL.\n
        'You have to login with proper credentials''', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(fun):
    """
    Auth decorator.
    """
    @wraps(fun)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return unauthenticate()
        return fun(*args, **kwargs)
    return decorated

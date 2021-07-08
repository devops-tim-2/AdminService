from exception.exceptions import InvalidAuthException, InvalidDataException, NotFoundException
from flask_restful import Resource, reqparse
from flask import request
from common.utils import auth
from exception.exceptions import InvalidAuthException, InvalidCredentialsException, NotFoundException
from service import admin_service, user_service

login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str, help='Username for user account (login)', required=True)
login_parser.add_argument('password', type=str, help='Password for user account (login)', required=True)

register_parser = reqparse.RequestParser()
register_parser.add_argument('username', type=str, help='Username for user account (register)', required=True)
register_parser.add_argument('password', type=str, help='Password for user account (register)', required=True)

 
class ApproveResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self, agent_id):
        try:
            if not request.headers.has_key('Authorization'):
                return 'Forbidden, unauthorized atempt.', 403
            else:
                token = request.headers['Authorization'].split(' ')[1]
                user = auth(token)

                return admin_service.approve(agent_id, user), 200
        except InvalidAuthException as e:
            return str(e), 401
        except NotFoundException as e:
            return str(e), 404

class RejectResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self, agent_id):
        try:
            if not request.headers.has_key('Authorization'):
                return 'Forbidden, unauthorized atempt.', 403
            else:
                token = request.headers['Authorization'].split(' ')[1]
                user = auth(token)

                return admin_service.reject(agent_id, user), 200
        except InvalidAuthException as e:
            return str(e), 401
        except NotFoundException as e:
            return str(e), 404

class BanResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self, user_id):
        try:
            if not request.headers.has_key('Authorization'):
                return 'Forbidden, unauthorized atempt.', 403
            else:
                token = request.headers['Authorization'].split(' ')[1]
                user = auth(token)

                return admin_service.ban(user_id, user), 200
        except InvalidAuthException as e:
            return str(e), 401
        except NotFoundException as e:
            return str(e), 404

class DeleteResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self, post_id):
        try:
            if not request.headers.has_key('Authorization'):
                return 'Forbidden, unauthorized atempt.', 403
            else:
                token = request.headers['Authorization'].split(' ')[1]
                user = auth(token)

                return admin_service.delete(post_id, user), 200
        except InvalidAuthException as e:
            return str(e), 401
        except NotFoundException as e:
            return str(e), 404
 
class LoginResource(Resource):
    def __init__(self):
        super().__init__()

    def post(self):
        args = login_parser.parse_args()

        try:
            return user_service.login(args), 200
        except InvalidCredentialsException as e:
            return str(e), 403

class RegisterResource(Resource):
    def __init__(self):
        super().__init__()

    def post(self):
        args = register_parser.parse_args()

        try:
            return user_service.register(args), 200
        except InvalidDataException as e:
            return str(e), 400
 
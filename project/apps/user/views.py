from flask_restful import Resource
from project.apps.user import api

class LoginResource(Resource):

    def get(self):
        return {'msg':'login success'}

api.add_resource(LoginResource,'/login')
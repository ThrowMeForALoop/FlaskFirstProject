from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        required=True,
                        type=str,
                        help='name should not be left empty')
    parser.add_argument('password', type=str, required=True,
                        help='password should not be left empty')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'User already created'}, 400

        new_user = UserModel(**data)
        new_user.save_to_db()

        return {'message': 'User created sucessfully'}, 201

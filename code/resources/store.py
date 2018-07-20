from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_store_by_name(name)
        if store:
            return {'store': store.json()}
        return {'message': 'store is not found'}, 404

    # def put(self, name):
    #     data = self.parser.parse_args()
    #     store = StoreModel.find_store_by_name(name)

    #     if store is None:
    #         store = StoreModel(**data)
    #     else:
    #         store.
    #     try:
    #         updated_store.save_to_db()
    #     except Exception as e:
    #         print(e)
    #         return {'message': 'Error upsert {}'.format(e)}, 500

    #     return updated_store.json()

    def post(self, name):
        if StoreModel.find_store_by_name(name):
            return {'message': 'store already exists'}, 400
        new_store = StoreModel(name)

        try:
            new_store.save_to_db()
        except Exception as e:
            print(e)
            return {'message': 'Error upsert {}'.format(e)}, 500

        return new_store.json()

    def delete(self, name):
        store = StoreModel.find_store_by_name(name)
        if store is None:
            store.delete_from_db()

        return {'message': 'store is deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}

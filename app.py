from flask import Flask
from flask_restful import Resource, Api
from db import *

app = Flask(__name__)
api = Api(app)

class RetailApp(Resource):
    def get(self,id):
        return get_data(id)

api.add_resource(RetailApp, '/products/<int:id>',methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
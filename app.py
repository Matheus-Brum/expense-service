from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from swagger_ui import api_doc
from api.routes.routes import health
from handler.expenseServiceHandler import Expenses, Expense

app_url_prefix: str = '/v1'
app: Flask = Flask(__name__)
api: Api = Api(app, prefix=app_url_prefix)
CORS(app)

app.register_blueprint(health, url_prefix=app_url_prefix)
api.add_resource(Expenses, '/expenses')
api.add_resource(Expense, '/expenses/<expense_id>')
api_doc(app, config_path='./docs/openapi/expenseApiDefinition.yaml',
        url_prefix=app_url_prefix + '/api/doc', title='API doc')

if __name__ == '__main__':
    app.run(debug=True, port=8080)

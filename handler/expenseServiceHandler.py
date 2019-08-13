from flask_restful import Resource
from flask import jsonify, abort, make_response, request
from uuid import uuid4
from api.models.expenseModel import ExpenseModel
from database.expenseDAO import ExpenseDAO
from mapper.expenseMapper import ExpenseMapper
from validators.expenseModelValidator import ExpenseModelValidator
from validators.commonValidator import CommonValidator


class Expenses(Resource):

    def __init__(self):
        self.expenseDAO: ExpenseDAO = ExpenseDAO()
        self.expense_mapper: ExpenseMapper = ExpenseMapper()

    def get(self):
        if request.args.get('user_id'):
            user_id = request.args.get('user_id')
            user_expenses = self.expenseDAO.retrieve_user_expenses(user_id)
            if user_expenses:
                return make_response(jsonify([self.expense_mapper.to_model(expense_entity).serialize()
                                              for expense_entity in user_expenses]), 200)
            abort(404)
        else:
            return [self.expense_mapper.to_model(expense_entity).serialize()
                    for expense_entity in self.expenseDAO.retrieve_expenses()]
        abort(404)

    def post(self):
        new_expense: ExpenseModel = ExpenseModel()
        new_expense.id = str(uuid4())
        new_expense.user_id = request.json['userId']
        new_expense.category = request.json['category']
        new_expense.name = request.json['name']
        new_expense.amount = request.json['amount']
        if ExpenseModelValidator.validate_expense_model(new_expense):
            is_expense_added: bool = self.expenseDAO.add_expense(new_expense)
            if is_expense_added:
                return make_response(jsonify(new_expense.serialize()), 201)
            print('unexpected error occurred.')
            abort(500)
        print('invalid expense model.')
        abort(400)


class Expense(Resource):

    def __init__(self):
        self.expenseDAO: ExpenseDAO = ExpenseDAO()
        self.expense_mapper: ExpenseMapper = ExpenseMapper()

    def get(self, expense_id: str):
        if not CommonValidator.is_none(expense_id) and CommonValidator.validate_id(expense_id):
            expense_entity = self.expenseDAO.retrieve_expense(expense_id)
            if expense_entity:
                return make_response(jsonify(self.expense_mapper.to_model(expense_entity).serialize()), 200)
            print('no expense found.')
            abort(404)
        print('invalid expense id.')
        abort(400)

    def delete(self, expense_id: str):
        if not CommonValidator.is_none(expense_id) and CommonValidator.validate_id(expense_id):
            expense_entity = self.expenseDAO.retrieve_expense(expense_id)
            if expense_entity:
                is_expense_removed: bool = self.expenseDAO.remove_expense(expense_id)
                if is_expense_removed:
                    return make_response(jsonify(self.expense_mapper.to_model(expense_entity).serialize()), 200)
                print('unexpected error occurred.')
                abort(500)
            print('no expense found.')
            abort(404)
        print('invalid expense id.')
        abort(400)

    def put(self, expense_id: str):
        print('invalid expense id or expense model.')
        abort(400)
        pass

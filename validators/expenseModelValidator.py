from validators.commonValidator import CommonValidator
from api.models.expenseModel import ExpenseModel


class ExpenseModelValidator:

    @staticmethod
    def validate_expense_model(expense_model: ExpenseModel) -> bool:
        return not CommonValidator.is_none(expense_model) and not CommonValidator.is_empty(expense_model) and \
                not CommonValidator.is_none(expense_model.id) and not CommonValidator.is_none(expense_model.user_id) and \
                not CommonValidator.is_none(expense_model.category) and not CommonValidator.is_none(expense_model.name) and \
                not CommonValidator.is_none(expense_model.amount) and not CommonValidator.is_empty(expense_model.id) and \
                not CommonValidator.is_empty(expense_model.user_id) and not CommonValidator.is_empty(expense_model.category) and \
                not CommonValidator.is_empty(expense_model.name) and not CommonValidator.is_empty(expense_model.amount) and \
                CommonValidator.validate_id(expense_model.id) and CommonValidator.validate_id(expense_model.user_id) and \
                CommonValidator.validate_string(expense_model.category, 1, 128) and CommonValidator.validate_string(expense_model.name, 1, 128) and \
                CommonValidator.validate_number(expense_model.amount)

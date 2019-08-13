from api.models.expenseModel import ExpenseModel


class ExpenseMapper:

    def to_model(self, expense_entity) -> ExpenseModel:
        expense_model: ExpenseModel = ExpenseModel()
        if expense_entity:
            expense_model.id = expense_entity["Id"]
            expense_model.user_id = expense_entity["ExpenseUserId"]
            expense_model.category = expense_entity["Category"]
            expense_model.name = expense_entity["Name"]
            expense_model.amount = expense_entity["Amount"]
        return expense_model

    def to_entity(self):
        pass

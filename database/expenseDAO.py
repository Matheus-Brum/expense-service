import pymysql
from api.models.expenseModel import ExpenseModel
from config.expenseServiceConfig import ExpenseServiceConfiguration


class ExpenseDAO:

    def __init__(self):
        self.connection: pymysql.Connection = None
        self.expense_service_configuration: ExpenseServiceConfiguration = ExpenseServiceConfiguration()

    def create_connection(self) -> pymysql.Connection:
        try:
            if not self.connection:
                self.connection = pymysql.connect(host=self.expense_service_configuration.instance.HOST,
                                                  user=self.expense_service_configuration.instance.USER,
                                                  password=self.expense_service_configuration.instance.PASSWORD,
                                                  db=self.expense_service_configuration.instance.DB,
                                                  charset=self.expense_service_configuration.instance.CHARSET,
                                                  cursorclass=pymysql.cursors.DictCursor)
            return self.connection
        except pymysql.MySQLError as err:
            print("expense service create_connection error : ")
            print(err)
            return None

    def retrieve_expenses(self):
        try:
            cursor = self.create_connection().cursor()
            cursor.execute("SELECT * "
                           "FROM expense")
            result = cursor.fetchall()
            return result
        except pymysql.MySQLError as err:
            print("expense service retrieve_expenses error : ")
            print(err)
            return None

    def add_expense(self, expense_model: ExpenseModel) -> bool:
        try:
            cursor = self.create_connection().cursor()
            cursor.execute("INSERT INTO expense (Id, ExpenseUserId, Category, Name, Amount)"
                           "VALUES(%s,%s,%s,%s,%s)", (expense_model.id, expense_model.user_id,
                                                      expense_model.category, expense_model.name, expense_model.amount))
            self.connection.commit()
            return True
        except pymysql.MySQLError as err:
            print("expense service add_expense error : ")
            print(err)
            return False

    def retrieve_expense(self, expense_id: str):
        try:
            cursor = self.create_connection().cursor()
            cursor.execute("SELECT * "
                           "FROM expense "
                           "WHERE Id = %s", (expense_id,))
            result = cursor.fetchone()
            return result
        except pymysql.MySQLError as err:
            print("expense service retrieve_expense error : ")
            print(err)
            return None

    def retrieve_user_expenses(self, user_id: str):
        try:
            cursor = self.create_connection().cursor()
            cursor.execute("SELECT * "
                           "FROM expense "
                           "WHERE ExpenseUserId = %s", (user_id,))
            result = cursor.fetchall()
            return result
        except pymysql.MySQLError as err:
            print("expense service retrieve_user_expenses error : ")
            print(err)
            return None

    def remove_expense(self, expense_id: str) -> bool:
        try:
            cursor = self.create_connection().cursor()
            cursor.execute("DELETE FROM expense "
                           "WHERE Id = %s", (expense_id,))
            self.connection.commit()
            return True
        except pymysql.MySQLError as err:
            print("expense service remove_expense error : ")
            print(err)
            return False

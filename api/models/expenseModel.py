class ExpenseModel:
    def __init__(self):
        self.id: str = None
        self.user_id: str = None
        self.category: str = None
        self.name: str = None
        self.amount: float = None

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "category": self.category,
            "name": self.name,
            "amount": self.amount
        }

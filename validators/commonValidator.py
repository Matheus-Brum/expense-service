from validator_collection import checkers
import uuid


class CommonValidator:

    @staticmethod
    def validate_string(string: str, min_len: int, max_len: int) -> bool:
        return checkers.is_string(string, minimum_length=min_len, maximum_length=max_len)

    @staticmethod
    def is_none(item) -> bool:
        return checkers.is_none(item)

    @staticmethod
    def is_empty(item) -> bool:
        return not checkers.is_not_empty(item)

    @staticmethod
    def validate_id(id: str) -> bool:
        try:
            id_object: uuid.UUID = uuid.UUID(id, version=4)
        except ValueError:
            return False
        return checkers.is_uuid(id) and str(id_object) == id

    @staticmethod
    def validate_number(number) -> bool:
        return checkers.is_numeric(number)

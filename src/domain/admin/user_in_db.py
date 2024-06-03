from src.domain.admin.user import User


class UserInDB(User):
    hashed_password: str

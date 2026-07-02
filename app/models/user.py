from datetime import datetime, date


class User:
    def __init__(
            self,
            id: int,
            email: str,
            first_name: str,
            last_name: str,
            hashed_password: str,
            date_of_birth: date | None,
            created_at: datetime,
            updated_at: datetime
        ):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.hashed_password = hashed_password
        self.date_of_birth = date_of_birth
        self.created_at = created_at
        self.updated_at = updated_at
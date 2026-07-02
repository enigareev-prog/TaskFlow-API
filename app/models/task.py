from datetime import datetime, timezone


class Task:
    def __init__(
            self, 
            id: int, 
            title: str, 
            description: str | None, 
            priority: str, 
            status:str, 
            created_at: datetime, 
            updated_at: datetime
        ):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
    

    def update(self, update_data: dict):
        for key, value in update_data.items():
            setattr(self, key, value)
        
        self.updated_at = datetime.now(timezone.utc)


    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

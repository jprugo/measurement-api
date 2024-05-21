from masoniteorm.models import Model
from datetime import datetime

class Alarm(Model):
    """Alarm Model"""
    id: int
    name: str
    created_at: datetime
    __timestamps__ = False
from masoniteorm.models import Model

class Isolation(Model):
    """Isolation Model"""
    __tablename__ = 'Isolation'
    id: int
    value: float
    created_at: str
    __timestamps__ = False
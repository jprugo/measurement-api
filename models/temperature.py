from masoniteorm.models import Model


class Temperature(Model):
    """Temperature Model"""
    __tablename__ = 'Temperature'
    id: int
    value: float
    created_at: str
    type: str
    __timestamps__ = False
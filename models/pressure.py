from masoniteorm.models import Model


class Pressure(Model):
    """Pressure Model"""
    __tablename__ = 'Pressure'
    id: int
    value: float
    created_at: str
    type: str
    __timestamps__ = False
from masoniteorm.models import Model


class Vibration(Model):
    """Vibration Model"""
    __tablename__ = 'Vibration'
    id: int
    value: float
    created_at: str
    type: str
    __timestamps__ = False
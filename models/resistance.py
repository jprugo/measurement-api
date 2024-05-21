from masoniteorm.models import Model


class Resistance(Model):
    """Resistance Model"""
    __tablename__ = 'Resistance'
    id: int
    value: float
    created_at: str
    type: str
    __timestamps__ = False
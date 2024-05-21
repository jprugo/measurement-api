from masoniteorm.models import Model

class Configuration(Model):
    """Configuration Model"""
    id: int
    name: str
    value: str
    __timestamps__ = True
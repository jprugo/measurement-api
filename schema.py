from datetime import datetime
from typing import Optional
import strawberry

# Type
@strawberry.type
class TemperatureType:
    id: int
    value: float
    created_at: str
    type: str

@strawberry.type
class IsolationType:
    id: int
    value: float
    created_at: str

@strawberry.type
class ResistanceType:
    id: int
    value: float
    created_at: str
    type: str

@strawberry.type
class VibrationType:
    id: int
    value: float
    created_at: str
    type: str

@strawberry.type
class PressureType:
    id: int
    value: float
    created_at: str
    type: str
    

# Input
@strawberry.input
class TemperatureInput():
    type: str
    value: float

@strawberry.input
class IsolationInput:
    value: float

@strawberry.input
class ResistanceInput:
    type: str
    value: float

@strawberry.input
class VibrationInput:
    type: str
    value: float

@strawberry.input
class PressureInput:
    type: str
    value: float

# Input filters
@strawberry.input
class DateInputFilter:
    start_date: datetime
    end_date: datetime

@strawberry.input
class FilterInput:
    created_at: DateInputFilter

@strawberry.input
class FilterInput2:
    created_at: DateInputFilter
    type: str

# Rest  schema

from pydantic import BaseModel

class ConfigurationType(BaseModel):
    name: str
    value: str

class ConfigurationType(BaseModel):
    name: str
    value: str

class AlarmType(BaseModel):
    name: str
    datetime: datetime

class DashBoardInfo(BaseModel):
    temperatureC: float
    temperatureM: float
    pressureC: float
    pressureD: float
    vibrationX: float
    vibrationZ: float
    fc: float
    vdC: float

class Drive(BaseModel):
    name: str

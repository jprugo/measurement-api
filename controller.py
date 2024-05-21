from typing import List
from datetime import datetime
from schema import DateInputFilter, IsolationInput, ResistanceInput, TemperatureInput, ResistanceType, IsolationType, TemperatureType, PressureInput, PressureType, VibrationInput, VibrationType
from models.temperature import Temperature
from models.isolation import Isolation
from models.resistance import Resistance
from models.vibration import Vibration
from models.pressure import Pressure

class BaseMutation:

    def _add_item(self, model_class, data):
        item = model_class()
        item.value = data.value
        item.created_at = datetime.now()
        if hasattr(data, 'type'):
            item.type = data.type
        item.save()
        return item

    def _get_all_items(self, model_class, **kwargs):
        query = model_class.select()
        
        for field, value in kwargs.items():
            if isinstance(value, DateInputFilter):
                query = query.where_between(field, value.start_date, value.end_date)
            else:    
                query = query.where(field, value)
                
        data = list(query.get())

        return data

class CreateMutation(BaseMutation):

    def add_temperature(self, data: TemperatureInput):
        return self._add_item(Temperature, data)

    def add_resistance(self, data: ResistanceInput):
        return self._add_item(Resistance, data)

    def add_isolation(self, data: IsolationInput):
        return self._add_item(Isolation, data)
    
    def add_vibration(self, data: VibrationInput):
        return self._add_item(Vibration, data)
    
    def add_pressure(self, data: PressureInput):
        return self._add_item(Pressure, data)


class Queries(BaseMutation):

    # Temperatures
    def get_all_temperatures(self, **kwargs) -> List[TemperatureType]:
        return self._get_all_items(Temperature, **kwargs)

    # Isolations
    def get_all_isolations(self, **kwargs) -> List[IsolationType]:
        return self._get_all_items(Isolation, **kwargs)
    
    # Resistances
    def get_all_resistances(self, **kwargs) -> List[ResistanceType]:
        return self._get_all_items(Resistance, **kwargs)
    
    # Vibrations
    def get_all_vibrations(self, **kwargs) -> List[VibrationType]:
        return self._get_all_items(Vibration, **kwargs)
    
    # Pressures
    def get_all_pressures(self, **kwargs) -> List[PressureType]:
        return self._get_all_items(Pressure, **kwargs)
from typing import List

import strawberry

from controller import CreateMutation, Queries
from schema import FilterInput, TemperatureType, ResistanceType, IsolationType, PressureType, VibrationType, FilterInput2

queries = Queries()  # Instancia de la clase Queries

@strawberry.type
class Mutation:
    create_mutation = CreateMutation()

    add_temperature: TemperatureType = strawberry.mutation(resolver=create_mutation.add_temperature)
    add_resistance: ResistanceType = strawberry.mutation(resolver=create_mutation.add_resistance)
    add_isolation: IsolationType = strawberry.mutation(resolver=create_mutation.add_isolation)
    add_vibration: IsolationType = strawberry.mutation(resolver=create_mutation.add_vibration)
    add_pressure: IsolationType = strawberry.mutation(resolver=create_mutation.add_pressure)



@strawberry.type(description="Measurements query", name="Measurement")
class Query:
    @strawberry.field(description="returns all the resistances from database and has the ability to filter through criteria")
    def getAllResistances(self, where: FilterInput2 = None) -> List[ResistanceType]:
        return queries.get_all_resistances(**vars(where))

    @strawberry.field(description="returns all the isolations from database and has the ability to filter through criteria")
    def getAllIsolations(self, where: FilterInput = None) -> List[IsolationType]:
        return queries.get_all_isolations(**vars(where))

    @strawberry.field(description="returns all the temperatures from database and has the ability to filter through criteria")
    def getAllTemperatures(self, where: FilterInput2 = None) -> List[TemperatureType]:
        return queries.get_all_temperatures(**vars(where))
    
    @strawberry.field(description="returns all pressures from database and has the ability to filter through criteria")
    def getAllPressures(self, where: FilterInput2 = None) -> List[PressureType]:
        return queries.get_all_pressures(**vars(where))
    
    @strawberry.field(description="returns all vibrations from database and has the ability to filter through criteria")
    def getAllVibrations(self, where: FilterInput2 = None) -> List[VibrationType]:
        return queries.get_all_vibrations(**vars(where))

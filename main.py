# Bp
from typing import List
import random
from datetime import datetime
# Server
import uvicorn
# Fast  API
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Strawberry - GraphQL
import strawberry
from strawberry.fastapi import GraphQLRouter
from core import Query, Mutation

# Configuration
from models.configuration import Configuration
from models.alarm import Alarm

# OP Model
from models.isolation import Isolation
from models.pressure import Pressure
from models.resistance import Resistance
from models.temperature import Temperature
from models.vibration import Vibration

# Schema
from schema import ConfigurationType, DashBoardInfo, AlarmType, Drive

from utils import write_to_csv

# USB
from pyudev import Context, Monitor, MonitorObserver, Device

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()

app.include_router(graphql_app, prefix="/measurement")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "200"}

@app.get("/getDashboardInfo")
def getDashboardInfo() -> DashBoardInfo:
    
    return DashBoardInfo(
        temperatureC= Temperature.where('type', 'C').last().value,
        temperatureM= Temperature.where('type', 'M').last().value,
        pressureC= Pressure.where('type', 'C').last().value,
        pressureD= Pressure.where('type', 'D').last().value,
        vibrationX= Vibration.where('type', 'X').last().value,
        vibrationZ= Vibration.where('type', 'Z').last().value,
        fc= random.uniform(5.0, 10.0),
        vdC= random.uniform(115, 120)
    )

@app.get("/configuration")
def getConfiguration()-> List[ConfigurationType]:
    dict = [ConfigurationType(name= c.name, value= c.value) for c in Configuration.all()]
    return dict

@app.get("/alarm")
def getAlarm()-> List[AlarmType]:
    dict = [AlarmType(name= c.name, datetime= c.created_at) for c in Alarm.all()]
    return dict

@app.get("/setup")
def setup():
    return {
        "voltaje": Configuration.where('name', 'voltage').first().value,
        "alarma" : Configuration.where('name', 'alarmValue').first().value, 
    }

@app.post("/alarm")
def createAlarm():
    alarm = Alarm()
    alarm.id = 0
    alarm.name = 'Alarma'
    alarm.save()

@app.post("/configuration")
def updateConfiguration(configuration: List[ConfigurationType]):
    for c in configuration:
        config_bd = Configuration.where('name', c.name).first()
        config_bd.value = c.value
        config_bd.updated_at = datetime.now()
        config_bd.save()
    return getConfiguration()

def _export_all_items(model_class, start_date: datetime, end_date: datetime, drive_name: str):
        file_name = f'/Volumes/{drive_name}/{model_class.__tablename__}.csv'
        data = model_class.select().where_between("created_at", start_date, end_date).get()
        write_to_csv(data, file_name)
        return data

@app.get("/exportIsolations")
def export_isolations(start_date: datetime, end_date: datetime, drive_name: str):
    _export_all_items(Isolation, start_date, end_date, drive_name)
    return 200

@app.get("/exportTemperatures")
def export_temperatures(start_date: datetime, end_date: datetime, drive_name: str):
    _export_all_items(Temperature, start_date, end_date, drive_name)
    return 200

@app.get("/exportVibrations")
def export_vibrations(start_date: datetime, end_date: datetime, drive_name: str):
    _export_all_items(Vibration, start_date, end_date, drive_name)
    return 200

@app.get("/exportPressures")
def export_pressures(start_date: datetime, end_date: datetime, drive_name: str):
    _export_all_items(Pressure, start_date, end_date, drive_name)
    return 200

@app.get("/exportResistances")
def export_resistances(start_date: datetime, end_date: datetime, drive_name: str):
    _export_all_items(Resistance, start_date, end_date, drive_name)
    return 200

def get_usb_drives() -> List[Drive]:
 
    drives = []
    try:
        context = Context()
        monitor = Monitor.from_netlink(context)
        monitor.filter_by(subsystem='usb')

        def callback(device: Device):
            if device.device_type == 'usb_device':
                drives.append(Drive(name=device.get('product')))

        observer = MonitorObserver(monitor, callback)
        observer.start()

        for device in context.list_devices(subsystem='usb'):
            if device.device_type == 'usb_device':
                drives.append(Drive(name=device.get('product')))

        return drives
    except:
        return [Drive(name= "SANDISK")]

@app.get("/drives")
async def get_drives() -> List[Drive]:
    return get_usb_drives()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
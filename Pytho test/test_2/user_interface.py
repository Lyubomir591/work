import data_prov 
import logg 

def temperatur (sensor):
    data = data_prov.get_temperature(sensor)
    logg.temperature_value(data)
    return data

def  preassure(sensor):
    data = data_prov.get_preassure(sensor)
    logg.temperature_value(data)
    return data


def speed (sensor):
    data = data_prov.get_wind_speed(sensor)
    logg.temperature_value(data)
    return data
from datetime import datetime as dt


def temperature_value(data):
    time = dt.now().strftime('%H:%M')
    with open('data_list.csv','a') as file:
        file.write(f'{time};temperature;{data}')

def preassure_value(data):
    time = dt.now().strftime('%H:%M')
    with open('data_list.csv','a') as file:
        file.write(f'{time};press;{data}')

def wind_speed_value(data):
    time = dt.now().strftime('%H:%M')
    with open('data_list.csv','a') as file:
        file.write(f'{time};speed;{data}')
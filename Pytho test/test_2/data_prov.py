from random import randint as randint

def get_temperature(sensor):
    return randint(-20, 0) if sensor else randint (0, 20 )

def get_preassure(sensor):
    if sensor :
        return randint(500, 550)
    else:
        return randint(550,600)
    
def get_wind_speed(sensor):
    if sensor == 1:
        return randint(0,30)
    else:
        return randint(30,60)
    
def collction(sensor = 1 ):
        return(get_temperature(sensor),get_preassure(sensor),get_wind_speed(sensor))
 
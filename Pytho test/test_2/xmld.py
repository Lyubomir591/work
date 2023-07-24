from user_interface import temperatur
from user_interface import preassure
from user_interface import speed




def createb(device=1):
    xml = '<xml>\n'
    xml += '    <temperature units = "c">{}</temperature>\n'\
        .format(temperatur(device))
    xml += '    <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(preassure(device))
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(speed(device))
    xml += '</xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)

    return xml
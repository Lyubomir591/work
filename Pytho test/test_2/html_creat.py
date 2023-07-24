from data_prov import get_temperature
from data_prov import get_preassure
from data_prov import get_wind_speed


def html_function(device = 1 ):
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(style, get_temperature(device))
    html += '    <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, get_wind_speed(device))
    html += '    <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, get_preassure(device))
    html += '  </body>\n</html>'
    
    with open('index.html', 'w') as page:
        page.write(html)

    return html
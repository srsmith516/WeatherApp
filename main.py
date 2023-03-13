import PySimpleGUI as sg
import WeatherData
0
weather_column = sg.Column([
    [sg.Image('',key = '-IMAGE-', background_color = '#FFFFFF',)]],
    key = '-LEFT-',
    background_color = '#FFFFFF')

info_column = sg.Column([
    [sg.Text('', key = '-LOCATION-', font = 'Calibri 30', background_color = '#FF0000', pad = 0, visible = False)],
    [sg.Text('', key = '-TEMP-', font = 'Calibri 16', pad = (0,10), background_color = '#FFFFFF', text_color = '#000000', justification = 'center', visible = False)]
    ],key = '-RIGHT-',
    background_color = '#FFFFFF')
 
main_layout = [
    [sg.Input(key = '-INPUT-',expand_x = True),sg.Button('submit', button_color = '#000000')],
    [weather_column,info_column]
]

sg.theme('reddit')
window = sg.Window('Weather', main_layout)
 
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
 
    if event == 'submit':
        #Get Locaiton
        Location = values['-INPUT-']
        #Get Weather by Location
        temp_celsius, temp_fahrenheit, feels_like_celsius, feels_like_fahrenheit, humidity, wind_speed, sunrise_time, sunset_time = WeatherData.get_weather_data(Location)
 
        window['-LOCATION-'].update("Home", visible = True)
        window['-TEMP-'].update(f'{temp_fahrenheit} \u2103 ({wind_speed})', visible = True)
 
        # sun
        #if weather in ('Sun','Sunny','Clear','Clear with periodic clouds', 'Mostly sunny'):
         #   window['-IMAGE-'].update('symbols/sun.png')
 
window.close()
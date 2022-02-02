import PySimpleGUI as sg
import sys
from pathlib import Path


def elige_carpeta(texto):
    sg.theme('Dark Blue 3')
    # Diseñamos el layout del cuadro de diálogo...
    layout = [  # FILA 1:
               [sg.Text(texto)],
               # FILA 2: el cuadro de entrada para el directorio, y el botón de explorar...
               [sg.Input(key='DIRECTORIO', default_text=''),
                sg.FolderBrowse('Explorar', initial_folder='')],
               # FILA 3: Los botones
               [sg.Button('Aceptar'), sg.Button('Salir')]]

    # Mostramos la ventana
    window = sg.Window('Elija la carpeta', layout)

    # Elegimos el directorio desde donde queremos buscar los ficheros
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Salir'):
            window.close()
            sg.Popup('Saliendo del programa')
            sys.exit()
        # Leemos el valor elegido...
        directorio = values['DIRECTORIO']
        # Creamos el objeto path con la elección del usuario
        # path_base = Path(directorio).resolve() si necesitáramos además que fuera absoluto
        path_base = Path(directorio)
        if path_base.exists():
            window.close()
            return directorio
        else:
            sg.Popup('El directorio indicado no existe')


def muestra_mensaje(texto):
    sg.Popup(texto)
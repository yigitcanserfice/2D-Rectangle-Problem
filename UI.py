import PySimpleGUI as sg

def get_coordinates():
    layout = [
        [sg.Text("1. Kenar:"), sg.InputText(key='x')],
        [sg.Text("2. Kenar:"), sg.InputText(key='y')],
        [sg.Button('Ekle'), sg.Button('Bitir')]
    ]

    window = sg.Window('Dikdörtgen Girişi', layout)

    coordinates = []

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Bitir':
            break

        try:
            x = int(values['x'])
            y = int(values['y'])
            coordinates.append((x, y))
            sg.popup(f"Dikdörtgen Eklendi: ({x}, {y})", auto_close_duration=1)

            # Input alanlarını temizle
            window['x'].update('')
            window['y'].update('')

            # X input alanına odaklan
            window['x'].set_focus()

        except ValueError:
            sg.popup_error("Geçersiz giriş. Lütfen sayısal değerler girin.")

    window.close()
    return coordinates


problem = get_coordinates()

print("Girilen Dikdörtgenler:")
print(problem)

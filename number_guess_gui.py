import PySimpleGUI as sg

# Function to generate a random number
import random

# Function to create the layout for the GUI
def create_layout():
    layout = [
        [sg.Text('Kérlek, adj egy számot 1 és 100 között:')],
        [sg.InputText(key='-INPUT-')] ,
        [sg.Button('Tipp'), sg.Button('Kilépés')],
        [sg.Text('', key='-OUTPUT-')]
    ]
    return layout

# Main function to run the GUI
def main():
    sg.theme('DarkAmber')  # Add a little color
    window = sg.Window('Számkitaláló', create_layout())
    random_number = random.randint(1, 100)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Kilépés':
            break
        try:
            guess = int(values['-INPUT-'])  # Get the guess input
            if guess < 1 or guess > 100:
                window['-OUTPUT-'].update('Kérlek, add meg a tippedet 1 és 100 között:\n')
            elif guess < random_number:
                window['-OUTPUT-'].update('Nagyobb!')
            elif guess > random_number:
                window['-OUTPUT-'].update('Kisebb!')
            else:
                window['-OUTPUT-'].update(f'Gratulálok, kitaláltad a számot! A gondolt szám: {random_number}.')
                random_number = random.randint(1, 100)  # Reset the game
        except ValueError:
            window['-OUTPUT-'].update('Helytelen adat! Kérlek, adj meg egy számot.\n')

    window.close()

if __name__ == '__main__':
    main()
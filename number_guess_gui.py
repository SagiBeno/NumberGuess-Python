import PySimpleGUI as sg
import random

# Set the theme
sg.theme('DarkBlue3')

def main():
    # Initialize the random number
    target_number = random.randint(1, 100)
    attempts = 0
    
    # Define the layout
    layout = [
        [sg.Text('Üdvözöllek a Számkitalálós játékban!', font=('Arial', 14, 'bold'))],
        [sg.Text('Gondoltam egy számra 1 és 100 között.', font=('Arial', 10))],
        [sg.Text('')],
        [sg.Text('Kérlek, add meg a tippedet:', font=('Arial', 10)), 
         sg.Input(key='-GUESS-', size=(10, 1), font=('Arial', 10))],
        [sg.Button('Tipp', size=(10, 1)), sg.Button('Újra kezd', size=(10, 1)), sg.Button('Kilépés', size=(10, 1))],
        [sg.Text('', size=(40, 1), key='-OUTPUT-', font=('Arial', 10), text_color='yellow')],
        [sg.Text('Próbálkozások:', font=('Arial', 10)), 
         sg.Text('0', key='-ATTEMPTS-', font=('Arial', 10), text_color='lightblue')],
    ]
    
    # Create the window
    window = sg.Window('Számkitalálós Játék', layout, finalize=True)
    window['-GUESS-'].focus()
    
    while True:
        event, values = window.read()
        
        if event == sg.WINDOW_CLOSED or event == 'Kilépés':
            break
        
        if event == 'Újra kezd':
            target_number = random.randint(1, 100)
            attempts = 0
            window['-GUESS-'].update('')
            window['-OUTPUT-'].update('')
            window['-ATTEMPTS-'].update('0')
            window['-GUESS-'].focus()
        
        if event == 'Tipp':
            guess_text = values['-GUESS-'].strip()
            
            # Validate input
            if not guess_text:
                window['-OUTPUT-'].update('Kérlek, adj meg egy számot!')
                continue
            
            if not guess_text.isdigit():
                window['-OUTPUT-'].update('Kérlek, csak számot adj meg!')
                continue
            
            guess = int(guess_text)
            
            # Check if the guess is in the valid range
            if guess < 1 or guess > 100:
                window['-OUTPUT-'].update('Kérlek, 1 és 100 közötti számot adj meg!')
                continue
            
            attempts += 1
            window['-ATTEMPTS-'].update(str(attempts))
            
            # Compare the guess with the target
            if guess < target_number:
                window['-OUTPUT-'].update('A tippelt szám kisebb, mint a gondolt szám.')
            elif guess > target_number:
                window['-OUTPUT-'].update('A tippelt szám nagyobb, mint a gondolt szám.')
            else:
                window['-OUTPUT-'].update(f'Gratulálok! {attempts} próbálkozásból kitaláltad a számot ({target_number})!')
                sg.popup_ok(f'Nyertél! {attempts} próbálkozás alatt!', title='Siker!')
                target_number = random.randint(1, 100)
                attempts = 0
                window['-GUESS-'].update('')
                window['-ATTEMPTS-'].update('0')
            
            window['-GUESS-'].update('')
            window['-GUESS-'].focus()
    
    window.close()

if __name__ == '__main__':
    main()
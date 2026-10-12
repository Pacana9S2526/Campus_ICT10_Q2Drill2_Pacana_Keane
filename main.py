# Finding club members
from pyscript import display, document

def club_finder(e):
    document.getElementById('result').innerHTML = ' '
    first_name = document.getElementById('firstname').value.lower().strip()
    last_name = document.getElementById('lastname').value.lower().strip()
    name = first_name + ' ' + last_name
    club_members = ["mj arbison", "basty uclaray", "cody deocampo", "bonnie nubla", "alexa agnote", "aisha padua"]
    club_checker = name in club_members

    display_message = (f'Sorry, there is no {name} in pigeon club :( join next year', f'{name} is in the pigeon club, congrats :)')
    display(display_message[club_checker], target='result')

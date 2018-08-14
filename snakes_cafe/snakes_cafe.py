from textwrap import dedent
import sys


WIDTH = 96

MENU = [{
    'apps': {
        'Wings': 0,
        'Chilli': 0,
        'Onion rings': 0,
    },

    'entrees': {
        'Crab legs': 0,
        'Buscuits and gravy': 0,
        'Pizza': 0,
    },

    'desserts': {
        'Peach cobbler': 0,
        'Apple pie': 0,
        'Cake': 0,
    },

    'drinks': {
        "Cavatica stout": 0,
        "Mannys": 0,
        "Vortex IPA": 0,
        "Water": 0,
    },
}
]


def greeting():
    """Function which will greet the user when run
    """
    ln_one = 'Welcome to Snakes Cafe!'
    ln_two = 'See menu below.'
    ln_three = 'To quit at anytime, type "quit"'

    print(dedent(f'''
        {'*' * WIDTH}
        {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one + (' ' * ((WIDTH - len(ln_one)) // 2))}
        {(' ' * ((WIDTH - len(ln_two)) // 2)) + ln_two + (' ' * ((WIDTH - len(ln_two)) // 2))}
        {(' ' * ((WIDTH - len(ln_three)) // 2)) + ln_three + (' ' * ((WIDTH - len(ln_three)) // 2))}
        {'*' * WIDTH}
    '''))


def menu():
    """Function will print the menu for the user to view
    """
    menu = 'MENU'

    apps = '''
    Appetizers\n
    ----------
    Wings\n
    Chilli\n
    Onion Rings\n
    '''

    entrees = '''
    Entrees\n
    ----------
    Crab legs\n
    Buscuits and gravy\n
    Pizza\n
    '''

    desserts = '''
    Desserts\n
    ----------
    Peach cobbler\n
    Apple Pie\n
    Cake\n
    '''

    drinks = '''
    Drinks\n
    ----------
    Cavatica stout\n
    Mannys\n
    Vortex IPA\n
    Water\n
    '''

    print(dedent(f'''
        {'*' * WIDTH}
        {(' ' * ((WIDTH - len(menu)) // 2)) + menu + (' ' * ((WIDTH - len(menu)) // 2))}
        {(' ' * ((WIDTH - len(apps)) // 2)) + apps + (' ' * ((WIDTH - len(apps)) // 2))}
        {(' ' * ((WIDTH - len(entrees)) // 2)) + entrees + (' ' * ((WIDTH - len(entrees)) // 2))}
        {(' ' * ((WIDTH - len(desserts)) // 2)) + desserts + (' ' * ((WIDTH - len(desserts)) // 2))}
        {(' ' * ((WIDTH - len(drinks)) // 2)) + drinks + (' ' * ((WIDTH - len(drinks)) // 2))}
        {'*' * WIDTH}
    '''))


def order():
    """Allows user to place an order from the menu
    """
    question = 'What can i get you?'

    print(dedent(
        question
    ))


def exit():
    """Allows the user to peacefully exit the application
    """
    print(dedent('''
        What no tip?!
    '''))
    sys.exit()


if __name__ == '__main__':
    greeting()
    menu()
    order()
    # print(MENU)

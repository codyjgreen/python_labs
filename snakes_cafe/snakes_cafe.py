from textwrap import dedent
import sys


WIDTH = 96


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


def exit():
    print(dedent('''
        What no tip?!
    '''))
    sys.exit()


if __name__ == '__main__':
    greeting()
    menu()

from . import setup,tools
from .states import main_menu,load_screen,level1
from . import constants as c



def main():
    """Add states to control here."""
    while(1):
        run_it = tools.Control(setup.ORIGINAL_CAPTION)
        state_dict = {c.LEVEL1: level1.Level1()}
        run_it.setup_states(state_dict, c.LEVEL1)
        current_run = run_it.main()
        if current_run['mario dead']:
            print("Dead")
        else:
            print("We gucci")



        # state_dict = {c.MAIN_MENU: main_menu.Menu(),
        #               c.LOAD_SCREEN: load_screen.LoadScreen(),
        #               c.TIME_OUT: load_screen.TimeOut(),
        #               c.GAME_OVER: load_screen.GameOver(),
        #               c.LEVEL1: level1.Level1()}
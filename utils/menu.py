from colorama import Fore, Style

def option_element(order: str, option: str, ending: str=' '):
    #print(f"{Fore.CYAN}[{Fore.CYAN}{Style.RESET_ALL}{order}{Style.RESET_ALL}{Fore.CYAN}]{Fore.CYAN}{Style.RESET_ALL}{option} ", end=ending)
    print(Fore.CYAN +'[ ' +Fore.CYAN +Style.RESET_ALL \
        +str(order) +Style.RESET_ALL \
        +Fore.CYAN +' ] ' +Fore.CYAN +Style.RESET_ALL \
        +option, end=ending)

def option_menu():
    option_element(1, "Crear", ', ')
    option_element(2, "Eliminar", ', ')
    option_element(3, "Actualizar", ', ')
    option_element(4, "Salir", '\n')
    print(Fore.YELLOW +'Elija opción:' +Style.RESET_ALL)
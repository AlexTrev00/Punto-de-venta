from colorama import Fore, Style
from funciones import add_products, show_productos, file_path, delete_products, find_product, product_sell
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
import json

def banner ():
    font = f''' {Fore.GREEN}

 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |      __      | || |     _____    | || |      __      | |
| |   .' ___  |  | || |     /  \     | || |    |_   _|   | || |     /  \     | |
| |  / .'   \_|  | || |    / /\ \    | || |      | |     | || |    / /\ \    | |
| |  | |         | || |   / ____ \   | || |   _  | |     | || |   / ____ \   | |
| |  \ `.___.'\  | || | _/ /    \ \_ | || |  | |_' |     | || | _/ /    \ \_ | |
| |   `._____.'  | || ||____|  |____|| || |  `.___.'     | || ||____|  |____|| |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 

{Style.RESET_ALL}'''
    print(font)

def menu():
    opciones = ['agregar productos','ver productos', 'Eliminar Producto','Buscar Producto','venta de productos']
    while True:
        print(f''' {Fore.YELLOW}
        1) {opciones[0]}

        2) {opciones[1]}

        3) {opciones[2]}

        4) {opciones[3]}

        5) {opciones[4]}

        6) Exit
''')
        user = int(input(f"eliga una opcion > {Fore.GREEN}"))
        if user == 1:
            add_products(file_path)
        elif user == 2:
            show_productos(file_path)
        elif user == 3:
            with open(file_path,'r') as file:
                productos = json.load(file)
            completer = WordCompleter(productos, ignore_case=True)
            session = PromptSession()
            print(f"{Fore.LIGHTYELLOW_EX}presione tab para ver los productos")
            delete_element = session.prompt('escribe una palabra: ', completer=completer)
            delete_products(file_path, delete_element)           
        elif user == 4:
            with open(file_path,'r') as file:
                productos = json.load(file)
            completer = WordCompleter(productos, ignore_case=True)
            session = PromptSession()
            print(f"{Fore.LIGHTYELLOW_EX}Presione Tab para ver un listado de los productos")
            product = session.prompt("escriba el producto que desee buscar: ", completer=completer)
            find_product(file_path, product)
        elif user == 5:
            product_sell(file_path)
        elif user == 6:
            break
        else:
            print("esa no es una opcion")
if __name__==__name__:
    banner()
    menu()


    
    

import json
from colorama import Fore
import difflib
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

def add_products(file_path):
    try: 
        with open(file_path, 'r') as file:
            productos = json.load(file)
    except FileNotFoundError:
        productos={}
    while True:
        user_product= input("ingrese el producto: ")
        user_price = float(input("ingrese el precio del producto: "))
        productos[user_product]= user_price
        control = input("¿desea ingresar mas productos? s para si / n para no: ").lower()
        if control == 'n':
            control= False
            break
    with open(file_path,'w') as file:
        json.dump(productos, file, indent=4)

file_path='productos.json'    

def show_productos(file_path):
    try:
        with open(file_path,'r') as file:
            productos = json.load(file)
            for x,y in productos.items():
                print(Fore.LIGHTBLUE_EX,x,':',y)
    except FileNotFoundError as e:
        print(f"el archivo JSON no existe {e}")

def delete_products(file_path, delete_element):
    try:
        with open(file_path,'r') as file:
            productos = json.load(file)
    except FileNotFoundError as e:
        print(f"El archivo no existe {e}")
        return
    except json.JSONDecodeError as f:
        print(f"el archivo no tiene un formato JSON valido {f}")
        return
    if delete_element in productos:
        del productos[delete_element]
        print(f"{Fore.RED}se elimino el producto {delete_element}")
        with open(file_path, 'w') as file:
            json.dump(productos, file, indent=4)
            for v,k in productos.items():
                print(Fore.LIGHTBLUE_EX,v,':',k)
    else:
        print(f"el producto {delete_element} no esta en el inventario")

def find_product(file_path,product):
    with open(file_path,'r') as file:
        productos = json.load(file)
    if product in productos:
        print(productos[product])
    else:
        print(f"el producto {product} no esta en el inventario")

def product_sell(file_path):
    with open(file_path, 'r') as file:
        productos = json.load(file)
    show_productos(file_path)
    ventas = []
    while True:
        completer = WordCompleter(productos, ignore_case=True)
        session = PromptSession()
        print(f"{Fore.LIGHTYELLOW_EX}presion Tab para ver un listado de los productos")
        producto = session.prompt("ingrese el prducto: ", completer=completer)
        if producto in productos:
            ventas.append(productos[producto])
            control = input(f"{Fore.LIGHTRED_EX}hay otro producto? s para si / n para no: ").lower()
            if control == 'n':
                suma = sum(ventas)
                print(f"{Fore.LIGHTMAGENTA_EX} Total: ${suma} pesos")
                input(f"{Fore.LIGHTBLUE_EX}Presione enter para continuar")
                user = float(input('con cuanto pago el cliente?: '))
                cambio = user - suma
                if cambio < 0:
                    print(f"{Fore.LIGHTRED_EX} falta dinero")
                print(f"{Fore.LIGHTMAGENTA_EX}el cambio es de ${cambio:.2f} pesos")
                break
        else:
            print(f'{Fore.LIGHTRED_EX}el producto {producto} no esta en el inventario')    
    

    


    






    


    




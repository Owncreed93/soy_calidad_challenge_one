from colorama import Fore, Style
# from tabulate import tabulate

from soy_calidad_challenge_1.product_manager import ProductManager
from soy_calidad_challenge_1.product import Product
from utils.menu import option_menu


# Inicializamos una instancia de ProductManager
product_manager = ProductManager()


print(Fore.GREEN + Style.BRIGHT + "--- Gestión de Productos ---" + Style.RESET_ALL)

option_menu()

try:
    product = Product('Pantalón Levy', 20, 40)
    product_manager.add_product(product)
    
except Exception as e:
    print(f'Error: {e}')
else:
    # print(product)
    product_manager.read_products()


# while True:
#     try:
#         opcion = int(input(Fore.YELLOW + "Selecciona una opción (1-5): " + Style.RESET_ALL))

#         if opcion == 1:
#             nombre = input("Nombre del producto: ")
#             precio = float(input("Precio del producto: "))
#             stock = int(input("Cantidad en stock: "))
#             product_manager.create_product(nombre, precio, stock)
#             print(Fore.GREEN + "Producto creado con éxito!" + Style.RESET_ALL)

#         elif opcion == 2:
#             productos = product_manager.read_products()
#             if productos:
#                 print(tabulate(productos, headers="keys", tablefmt="fancy_grid"))
#             else:
#                 print(Fore.RED + "No hay productos registrados." + Style.RESET_ALL)

#         elif opcion == 3:
#             product_id = int(input("ID del producto a actualizar: "))
#             nombre = input("Nuevo nombre (deja vacío para no cambiar): ")
#             precio = input("Nuevo precio (deja vacío para no cambiar): ")
#             stock = input("Nuevo stock (deja vacío para no cambiar): ")
#             product_manager.update_product(product_id, nombre or None, float(precio) if precio else None, int(stock) if stock else None)

#         elif opcion == 4:
#             product_id = int(input("ID del producto a eliminar: "))
#             product_manager.delete_product(product_id)

#         elif opcion == 5:
#             print(Fore.BLUE + "Saliendo del programa..." + Style.RESET_ALL)
#             break

#         else:
#             print(Fore.RED + "Opción no válida." + Style.RESET_ALL)

#     except ValueError:
#         print(Fore.RED + "Por favor, introduce un número válido." + Style.RESET_ALL)

#     except Exception as e:
#         print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)
from colorama import Fore, Style

from soy_calidad_challenge_1.product_manager import ProductManager
from soy_calidad_challenge_1.product import Product
from utils.menu import option_menu, show_table


product_manager = ProductManager()

print(Fore.GREEN + Style.BRIGHT + "--- Gestión de Productos ---" + Style.RESET_ALL)

while True:
    try:
        products = product_manager.read_products()
        show_table(products)
        option_menu()
        opcion = int(input(Fore.YELLOW + 'Elija la opción: ' + Style.RESET_ALL))
        print('\n')

        if opcion == 1:
            name = input('Nombre del producto: ')
            price = float(input('Precio del producto: '))
            stock = int(input('Cantidad en stock: '))
            product = Product(name, price, stock)
            product_manager.add_product(product)
            print(Fore.GREEN + '!Producto creado con éxito! \n' + Style.RESET_ALL)

        elif opcion == 2:
            product_id = int(input('ID del producto a eliminar: '))
            if product_manager.delete_product(product_id):
                print(Fore.GREEN + '!Producto eliminado con éxito!' + Style.RESET_ALL)
            else:
                print(Fore.RED + 'Error al actualizar, revisa los datos enviados.' + Style.RESET_ALL)

        elif opcion == 3:
            product_id = int(input('ID del producto a actualizar: '))
            nombre = input('Nuevo nombre (deja vacío para no cambiar): ')
            precio = input('Nuevo precio (deja vacío para no cambiar): ')
            stock = input('Nuevo stock (deja vacío para no cambiar): ')
            result = product_manager.update_product(product_id, nombre or None, 
                                        float(precio) if precio else None, 
                                        int(stock) if stock else None)
            if product_manager.delete_product(product_id):
                print(Fore.GREEN + '!Producto actualizado con éxito!' + Style.RESET_ALL)
            else:
                print(Fore.RED + 'Error al actualizar, revisa los datos enviados.' + Style.RESET_ALL)
                

        elif opcion == 4:
            print(Fore.BLUE + 'Saliendo del programa...' + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + 'Opción no válida.' + Style.RESET_ALL)
    
    except KeyboardInterrupt:
        print(Fore.BLUE + '\n Saliendo del programa (Interrupción de teclado)...' + Style.RESET_ALL)
        break

    except ValueError:
        print(Fore.RED + 'Por favor, introduce un número válido.' + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f'Error: {str(e)}' + Style.RESET_ALL)
from gestion_inv import consultar,registrar_inventario,eliminar_producto,actualizar_producto,mostrar
from consultas import registro_venta, mostrar_ventas, consult_sale,reporte_ingresos,reports_sales,reports_top
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def main():
    while True:
        print("Welcome to the national bookstore\n")
        print("1. Inventory management")
        print("2. Sales")
        print("3. Reports")
        print("4. Exit\n")

        option=input("Enter option: ")
        if option =="1":
            inventory_menu()
        elif option == "2":
            sales_menu()
        elif option == "3":
            report_menu()
        elif option == "4":
            print("Thanks")
            break
        else:
            print("Option not found")

def inventory_menu():
    while True:
        print("Welcome to the national bookstore\n")
        print("1. Record inventory")
        print("2. Check inventory")
        print("3. Show inventory")
        print("4. Update inventory")
        print("5. Delete inventory")
        print("6. Exit\n")            

        option=input("Enter option: ")
        if option =="1":
            registrar_inventario()
        elif option == "2":
            consultar()
        elif option == "3":
            mostrar()    
        elif option == "4":
            actualizar_producto()
        elif option == "5":
            eliminar_producto()
        elif option == "6":
            print("Thanks")
            break
        else:
            print("Option not found")
def report_menu():
    while True:
        print("Menu sales\n")
        print("1. Income report")
        print("2. Report sales")
        print("3. Report top")
        print("4. Exit\n")            

        option=input("Enter option: ")
        if option =="1":
            reporte_ingresos()
        elif option == "2":
            reports_sales()
        elif option == "3":
            reports_top()
        elif option == "4":
            print("Thanks")
            break
        else:
            print("Option not found")  

def sales_menu():
    while True:
        print("Menu reports\n")
        print("1. Record sales")
        print("2. Show sales")
        print("3. Check sales")
        print("4. Exit\n")            

        option=input("Enter option: ")
        if option =="1":
            registro_venta()
        elif option == "2":
            mostrar_ventas()
        elif option == "3":
            consult_sale()
        elif option == "4":
            print("Thanks")
            break
        else:
            print("Option not found")  



if __name__=="__main__":
    main()
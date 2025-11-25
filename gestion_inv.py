"""Registrar, consultar, actualizar y eliminar productos
    items=[título, autor, categoría, precio, cantidad en stock] """
"""   """
inventario=[
    {
            "id":1,
            "titulo":"cien años",
            "autor":"gabriel",
            "categoria":"cronica",
            "precio":25000,
            "cantidad":2
        },
        {   
            "id":2,
            "titulo":"angelmatica",
            "autor":"grinberg",
            "categoria":"psicologico",
            "precio":130000,
            "cantidad":6
        },
        {   
            "id":3,
            "titulo":"La expancion del presente",
            "autor":"grinberg",
            "categoria":"psicologico",
            "precio":35000,
            "cantidad":10
        },
        {   
            "id":4,
            "titulo":"cronicas de una muerte anunciada",
            "autor":"gabriel",
            "categoria":"cronica",
            "precio":20000,
            "cantidad":5
        },
        {   
            "id":5,
            "titulo":"sol",
            "autor":"blackovsky",
            "categoria":"ficcion",
            "precio":10000,
            "cantidad":20
        }
]

""""""
"""def validar_numero(texto, tipo=float):
    
        try:
            if tipo > 0:
                valor = tipo(input(texto))
                return valor
            print("numero invalido")    
            

        except TypeError as e:
            print(f"tipo de valor invalido {e}") 
        except ValueError as e:
            print("debe ser numerico")  """       

def crear_id():
    return max((int(item["id"]) for item in inventario), default=0) + 1

def registrar_inventario():
    global inventario        
    try:
        print("registro productos")
        titulo=input("Nombre: ") 
        autor=input("autor: ")
        categoria=input("tipo libro: ")
        precio=float(input("precio: "))
        cantidad=int(input("cantidad: "))
    except ValueError:
        print("no se admiten datos vacios.")

            
    nuevo={
            "id":crear_id(),
            "titulo":titulo,
            "autor":autor,
            "categoria":categoria,
            "precio":precio,
            "cantidad":cantidad
        }
        
    inventario.append(nuevo)
    print(f"id: {nuevo["id"]} registrado")
        



def consultar():
    id_con=int(input("Enter id: "))
    if not inventario:
         print("Empty list")
    for i in inventario:
        if i["id"] == id_con:
            print(f"ID: {i["id"]} | titulo: {i["titulo"]} | autor: {i["autor"]} | categoria: {i["categoria"]} | precio: {i["precio"]} | cantidad stock: {i["cantidad"]}") 
        else:    
            print("Invalid id")              
       
    

def mostrar():
    global inventario
    for i in inventario:
        print(f"ID: {i["id"]} | titulo: {i["titulo"]} | autor: {i["autor"]} | categoria: {i["categoria"]} | precio: {i["precio"]} | cantidad stock: {i["cantidad"]}")               

def actualizar_producto():
    global inventario
    mostrar()
    id_act = int(input("ID a actualizar: "))

    
    for inv in inventario:
        if inv["id"] == id_act:
            nuevo_titulo = input(f"titulo ({inv["titulo"]}): ") or inv["titulo"]
            nueva_autor= input(f"autor ({inv["autor"]}): ") or inv["autor"]
            nueva_categoria = input(f"categoria ({inv["categoria"]}): ") or inv["categoria"]        
            nuevo_precio = float(input(f"nuevo precio ({inv["precio"]}): "))
            nueva_cantidad = int(input(f"nuevo stock ({inv["cantidad"]}): ")) 
            inv["titulo"]=nuevo_titulo
            inv["autor"]=nueva_autor
            inv["categoria"]=nueva_categoria
            inv["precio"]=nuevo_precio
            inv["cantidad"]=nueva_cantidad 
           

            print(f"ID: {inv["id"]} | title: {inv["titulo"]} | author: {inv["autor"]} | category: {inv["categoria"]} | price: {inv["precio"]} | amount stock: {inv["cantidad"]}")
    print("Actualizado correctamente.")     

def eliminar_producto():
    numero = int(input("ID delete: "))
    for inv in inventario:
        if inv["id"] == numero:
            inventario.remove(inv)
    print(f"Product with id {inv["id"]} delete")
            

         






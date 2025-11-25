from datetime import datetime
from gestion_inv import crear_id, mostrar, inventario

sales=[
    {
        "id":1,
        "id_inv":1,
        "cliente":"carlos",
        "tipo_cliente":"VIP",
        "producto":"La expancion del presente",
        "cantidad":2,
        "fecha":2025-12-10,
        "descuento":20,
        "total_neto":10000,
        "total_descuento":8000
    },
    {
        "id":2,
        "id_inv":2,
        "cliente":"mateo",
        "tipo_cliente":"normal",
        "producto":"sol",
        "cantidad":1,
        "fecha":2025-12-12,
        "descuento":5,
        "total_neto":10000,
        "total_descuento":9000
    },
    {
        "id":4,
        "id_inv":1,
        "cliente":"daniel",
        "tipo_cliente":"VIP",
        "producto":"sol",
        "cantidad":2,
        "fecha":2025-12-11,
        "descuento":20,
        "total_neto":10000,
        "total_descuento":8000
    },
    {
        "id":5,
        "id_inv":1,
        "cliente":"carlos",
        "tipo_cliente":"normal",
        "producto":"La expancion del presente",
        "cantidad":2,
        "fecha":2025-12-10,
        "descuento":5,
        "total_neto":10000,
        "total_descuento":9000
    },
    {
        "id":6,
        "id_inv":1,
        "cliente":"sofia",
        "tipo_cliente":"normal",
        "producto":"cronicas de una muerte anunciada",
        "cantidad":2,
        "fecha":2025-12-10,
        "descuento":5,
        "total_neto":10000,
        "total_descuento":9000
    }
    
]

def registro_venta():
    global inventario
    mostrar()
    
    id_inv=int(input("Enter ID: "))
    cliente=input("client name: ") 
    cantidad=int(input("Amount: "))
    fecha=datetime.now().strftime("%Y-%m-%d")
    descuento=int(input("discount applied:"))
    
    for i in inventario:
        if i["id"]==id_inv:
            if cantidad > i["cantidad"]:
                print("quantity out of stock")
                return
            i["cantidad"]-=cantidad
             
     
    total_neto=(i["precio"] * cantidad)
    total= total_neto* (1 - descuento / 100) 

    new={
        "id":crear_id(),
        "id_inv":i["id"],
        "cliente":cliente,
        "tipo_cliente":"normal",
        "producto":i["titulo"],
        "cantidad":cantidad,
        "fecha":fecha,
        "descuento":descuento,
        "total_neto":total_neto,
        "total_descuento":total
    }    
    sales.append(new)
    print(f"id: {new["id"]} registered sale for product {i["titulo"]}")

def mostrar_ventas():
    global sales
    for i in sales:
        print(f"ID: {i["id"]:5} | customer: {i["cliente"]:15} | type customer: {i["tipo_cliente"]:10} | product: {i["producto"]:25} | total: {i["total_neto"]:8} total_discount: {i["total_descuento"]:8} | amount: {i["cantidad"]:8} | date: {i["fecha"]:8}")               

    
def consult_sale():
    global sales
    if not sales:
        print("Empty list")
    number=int(input("Enter id: "))
    for i in sales:
        if i["id"] == number:
            print(f"ID: {i["id"]} | cliente: {i["cliente"]} | tipo cliente: {i["tipo_cliente"]} | producto: {i["producto"]} | total: {i["total_descuento"]} | cantidad: {i["cantidad"]} | fecha: {i["fecha"]}")   

def reports_top():
    global sales
    global inventario
    if not sales:
        print("Empty list")
        return None
    count = {}
    

    for i in sales:
        count[i["producto"]] = count.get(i["producto"], 0) + i["cantidad"]
        
    

    ranking = sorted(count.items(), key=lambda x: x[1], reverse=True)

    print(f"Best sellers {ranking[0:3]}")


def reports_sales():
    totales = {}

    for e in sales:
        s = next(p["titulo"] for p in inventario if p["titulo"] == e["producto"])
        totales[s] = totales.get(s, 0) + e["total_descuento"]

        for e, total in totales.items():
            total
        print(f"{s}: ${total}")

def reports_income():

    bruto = sum(s["total_neto"] for s in sales)
    descuentos =sum(s["total_descuento"] for s in sales)
    

    print(f"Gross income: ${bruto}")
    print(f"Net discount (after discount): ${descuentos}")



    

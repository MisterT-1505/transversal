productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX3050'],
'2175HD': ['LENOVO', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX2050'],
'UWU131HD': ['HP', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
stock={'8475HD': [387990,10], '2175HD': [327990,4], 'UWU131HD': [310990,2]}

def stock_marca():
    marca_buscada=input("Ingresa la marca de la cual quieres revisar el stock: ").upper()
    stock_p=0
    for producto in productos.values():
        if marca_buscada in producto[0]:
            stock_p+=1
        else:
            print ("marca no encontrada")
    print (f"el stock restante es de {stock_p}")
def Busqueda_por_precio():
    while True:
        try:
            p_min=int(input("Ingresa el rango menor de precio: "))
            break
        except ValueError:
            print ("Ingresa un numero valido")
    while True:
        try:
            p_max=int(input("Ingresa el rango mayor de precio: "))
            break
        except ValueError:
            print ("Ingresa un numero valido")
    lista_producto_encontrado=[]
    for producto in stock.values():
        if producto[0] in range(p_min,p_max):
            for modelo in stock.items():
                lista_producto_encontrado.append(modelo[0])
            pass
    print (f"{lista_producto_encontrado}")
def actualizar_precio():
    pass
def main():
    while True:
        print ("-"*100)
        print ("1.Stock Marca")
        print ("2.Busqueda por precio")
        print ("3.Actualizar precio")
        print ("4.Salir")
        print ("-"*100)
        try:
            menu_eleccion=int(input("Ingresa tu eleccion: "))
            if menu_eleccion==1:
                stock_marca()
            elif menu_eleccion==2:
                Busqueda_por_precio()
            elif menu_eleccion==3:
                actualizar_precio()
            elif menu_eleccion==4:
                print ("Programa finalizado")
                break
            else:
                raise ValueError
        except ValueError:
            print ("Debe seleccionar una opción válida!!")
main()
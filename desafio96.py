producto = {
   101:{"Nombre:": "Aceite",
        "Precio:": "$300",
        "Cantidad:": "30 unidades"
   },

    102:{
    "Nombre:": "Jabón",
    "Precio:": "$150",
    "Cantidad:":"10 unidades"
    }   }

print("# Mostramos el inventario de productos sin modificar:")
print(producto)

print("==========================")
print("# Agregamos el nuevo producto:")
producto[103] = {"Nombre:":"Leche",
                 "Precio:":"$90",
                 "Cantidad:":"15"}
print(producto[103])
print("===========================")
print("# Modificamos el aceite") 
print("Aceite sin modificar es:")
print(producto[101]["Cantidad:"])
print("Modificando el aceite pasa a:")
producto[101]["Cantidad:"] = "20 unidades"
print(producto[101]["Cantidad:"])
print("===========================")
print("# Mostramos el valor de un diccionario, en este caso el precio del Jabón")
print(producto[102]["Precio:"])



Texto = input ("Ingrese las palabras que quiera, procedere a contarlas.")
#Nombramos las palabras que van a ser tomadas como números.
Palabras = Texto.split() 
#Contador en número de las palabras.
Cantidad = len(Palabras) 
print("En el texto puedo contar", Cantidad ,"palabras.")
print(" Y las palabras que conte son estas:" , Palabras)
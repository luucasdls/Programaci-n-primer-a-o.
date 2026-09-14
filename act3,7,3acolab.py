from collections import Counter

notas = [8, 7, 9, 6, 8, 10, 7, 8]

# Pregunta 1: promedio
promedio = sum(notas) / len(notas)
print("Promedio de la clase:", promedio)

# Pregunta 2: nota más baja y más alta
print("Nota más baja:", min(notas))
print("Nota más alta:", max(notas))

# Pregunta 3: nota que más se repite
contador = Counter(notas)
nota_mas_repetida = contador.most_common(1)[0][0]

print("Nota que más se repite:", nota_mas_repetida)
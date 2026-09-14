import array
ventas_mensuales = array.array('i', [120, 135, 150, 145, 160, 155, 130, 140, 125, 170, 160, 180])
total_anual = sum(ventas_mensuales)
print (("Venta generada en total anualmente:"),total_anual)

promedio_mensual = total_anual / len(ventas_mensuales)
print(("Venta promedio generada mensualmente:"), promedio_mensual)

mes_min = ventas_mensuales.index(min(ventas_mensuales)) + 1
mes_max = ventas_mensuales.index(max(ventas_mensuales)) + 1
print(f"Mes con la venta más baja: {mes_min} (Venta: {min(ventas_mensuales)} unidades)")
print(f"Mes con la venta más alta: {mes_max} (Venta: {max(ventas_mensuales)} unidades)")
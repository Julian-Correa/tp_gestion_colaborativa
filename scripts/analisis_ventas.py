
import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv("datos/ventas_2024.csv")

# Mostrar primeras filas
print(df.head())

# Calcular ventas totales
ventas_totales = df["sales_amount"].sum()

print("Ventas Totales:", ventas_totales)

# Agrupar ventas por fecha
ventas_por_fecha = df.groupby("sales_date")["sales_amount"].sum()

# Generar gráfico
ventas_por_fecha.plot(figsize=(10,5))

plt.title("Ventas por Fecha")
plt.xlabel("Fecha")
plt.ylabel("Monto de Ventas")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

print("Gráfico generado correctamente")

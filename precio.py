precio_original = float(input("Ingresa el precio del producto:"))
tipo_cliente = input("Ingresa el tipo de cliente (Regular, estudiante, senior,):").lower()
descuento = 0
if tipo_cliente== "estudiante":
    descuento = 0.15
elif tipo_cliente == "senior":
    descuento = 0.20
    precio_final = precio_original * (1-descuento)
    print(f"El precio final despues del descuento es: {precio_final:.2f}")
    
def obtener_moneda_origen():
    """
    Solicita al usuario seleccionar la moneda de origen.
    Returns:
        str: Código de la moneda seleccionada
    """
    print("\nMonedas disponibles:")
    print("1. Peso Colombiano (COP)")
    print("2. Peso Mexicano (MXN)")
    print("3. Yen Chino (RMB)")
    print("4. Euro (EUR)")
    
    while True:
        try:
            opcion = int(input("\nSeleccione la moneda de origen (1-4): "))
            if opcion in [1, 2, 3, 4]:
                return {1: 'COP', 2: 'MXN', 3: 'RMB', 4: 'EUR'}[opcion]
            print("Por favor seleccione una opción válida (1-4)")
        except ValueError:
            print("Error: Por favor ingrese un número válido")

def obtener_cantidad(moneda):
   
    while True:
        try:
            cantidad = float(input(f"Ingrese la cantidad en {moneda}: "))
            if cantidad < 0:
                print("Por favor ingrese una cantidad válida (mayor o igual a 0)")
                continue
            return cantidad
        except ValueError:
            print("Error: Por favor ingrese un valor numérico válido")

def convertir_moneda(cantidad, moneda_origen):
    tasas = {
        'RMB': {
            'COP': 571.97,  # 1 RMB = 571.97 COP
            'MXN': 2.81,  # 1 RMB = 2.81 MXN
            'EUR': 0.13,  # 1 RMB = 0.13 EUR
        },
        'EUR': {
            'COP': 571.97 / 0.13,  # 1 EUR = (571.97 COP / 0.13 EUR) ≈ 4400.54 COP
            'MXN': 2.81 / 0.13,  # 1 EUR = (2.81 MXN / 0.13 EUR) ≈ 21.62 MXN
            'RMB': 1 / 0.13,  # 1 EUR = 1 / 0.13 RMB ≈ 7.69 RMB
        },
        'COP': {
            'RMB': 1 / 571.97,  # 1 COP = 1 / 571.97 RMB ≈ 0.00175 RMB
            'EUR': 0.13 / 571.97,  # 1 COP = 0.13 / 571.97 EUR ≈ 0.000227 EUR
            'MXN': 2.81 / 571.97,  # 1 COP = 2.81 / 571.97 MXN ≈ 0.00491 MXN
        },
        'MXN': {
            'RMB': 1 / 2.81,  # 1 MXN = 1 / 2.81 RMB ≈ 0.356 RMB
            'EUR': 0.13 / 2.81,  # 1 MXN = 0.13 / 2.81 EUR ≈ 0.0463 EUR
            'COP': 571.97 / 2.81,  # 1 MXN = 571.97 / 2.81 COP ≈ 203.55 COP
        }
    }
    
    resultado = {}
    for moneda_destino in tasas[moneda_origen]:
        resultado[moneda_destino] = cantidad * tasas[moneda_origen][moneda_destino]
    
    return resultado

def mostrar_resultado(cantidad, moneda_origen, conversiones):
    
    simbolos = {
        'RMB': '¥',
        'EUR': '€',
        'COP': 'COP',
        'MXN': 'MXN'
    }
    
    print("\nResultados de la conversión:")
    print(f"{cantidad:,.2f} {moneda_origen} es equivalente a:")
    
    for moneda, valor in conversiones.items():
        if moneda != moneda_origen:
            simbolo = simbolos[moneda]
            print(f"{moneda}: {simbolo} {valor:,.2f}")

def main():
    """
    Función principal del programa.
    """
    print("=== Convertidor de Divisas ===")
    print("Conversión entre COP, MXN, RMB y EUR")
    print("==================================")
    
    while True:
        # Obtener moneda de origen
        moneda_origen = obtener_moneda_origen()
        
        # Obtener cantidad
        cantidad = obtener_cantidad(moneda_origen)
        
        # Realizar conversiones
        conversiones = convertir_moneda(cantidad, moneda_origen)
        
        # Mostrar resultados
        mostrar_resultado(cantidad, moneda_origen, conversiones)
        
        # Preguntar si desea realizar otra conversión
        continuar = input("\n¿Desea realizar otra conversión? (s/n): ").lower()
        if continuar != 's':
            break
        print("\n")

    print("\n¡Gracias por utilizar nuestro sistema de divisas!")

if __name__ == "__main__":
    main()
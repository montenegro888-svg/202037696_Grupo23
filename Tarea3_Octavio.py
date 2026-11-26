# Definición del diccionario anidado corregido del BME680
mapa_BME680 = {
    "0x60": {
        "status": True, 
        "calib_val": 12, 
        "limit": 100
    },
    "0x61": {
        "status": True, 
        "calib_val": 55, 
        "limit": 200
    },
    "0x62": {
        "status": False, 
        "calib_val": 88, 
        "limit": 90
    }
}

# Funcio de consulta con .get. 

def consultar_registros_BME680(direccion):
    """
    Consulata un registro del sensor por su direccion hexagecimal.
    Usa .get() para un acceso seguro evitando KeyError.
    Implementa un control numérico de intentos para evitar desbordamientos o bucles infinitos.
    """
            
    # Búsqueda segura utilizando el método .get()
    datos = mapa_BME680.get(direccion)
            
    if datos is None:
        print(f">>>[AVISO] La dirección o registro '{direccion}' no existe en el mapa de memoria.")   
        print(f" Direcciones validas: {', '.join(mapa_BME680.keys())}")  
        return False 
    else:        
        print(f"\n>>>[ÉXITO] Especificaciones encontradas para el registro '{direccion}':")
        # Mostrar ordenadamente los parámetros técnicos sub-claves
        print(f" {'Estado:':<18} {datos.get('status', 'N/D')}")
        print(f" {'Calibracion:':<18} {datos.get('calib_val', 'N/D')}")
        print(f" {'Limite:':<18} {datos.get('limit', 'N/D')}")
        return True

# Funcion para mostrar todo el mapa 
def mostrar_mapa_cmpleto():
    # Muestra todos los registros disponibles.
    print("\n" + "=" * 60)
    print("    MAPA DE REGISTRO SENSOR BME680")
    print("=" * 60)
    print(f" {'Direccion':<12}{'Estado':<8}{'Calibracion':<14}{'Limite':<12}")
    print("=" * 60)
    for direccion, datos in mapa_BME680.items():
        estado = str(datos.get('status', 'N/D'))
        calib = str(datos.get('calib_val', 'N/D'))
        limite = str(datos.get('limit', 'N/D'))
        
        print(f" {direccion:<12} {estado:<8} {calib:<14} {limite:<12}")
    print("=" * 60)

# Bucle de consulta
def main():
    print("\n" + "=" * 60)
    print("   SISTEMA DE CONSULATA DEL SENSOR BME680")
    print("=" * 60)

    # Muestra el mapa completo al inicio
    mostrar_mapa_cmpleto()

    # Controla el bucle de consulta
    Max_Consultas = 3
    Cont = 0

    print(f"\n Tiene un maximo de {Max_Consultas} consultas.")
    print("Escribe 'salir' para terminar. \n ")

    while Cont < Max_Consultas:
        direccion = input(f"[Consulta{Cont + 1}/{Max_Consultas}]"
                          f"Ingrese direccion hexadecimal (Ej. 0x60): ").strip()

        # Opcion de salida anticipada.
        if direccion.lower() == "salir":
            print("\n>>> Salir del sitema por solicitud el usuario. <<<")
            break

        # Valida que no este vacio.
        if not direccion:
            print("Ingresa una direccion, Intenta de nuevo.")
            continue

        # Realiza la consulta segura.
        consultar_registros_BME680(direccion)
        Cont += 1

        # Mensaje final.
        if Cont >= Max_Consultas:
            print(f"\n>>> Limite de {Max_Consultas} consultas alcanzado. sistema finalizado. <<<")
        else:
            print(f"\n>>> Sistema finalizado. Consultas realizadas: {Cont} <<<")   

if __name__ == "__main__":
    main()
    
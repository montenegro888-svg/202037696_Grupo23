def verificar_presion(presion_gas):
    presion = presion_gas
    for lectura in range(10):
        if presion >= 6.0:
            print("CRITICO: Ruptura inminente.Abortar.")
            break
        if presion < 2.0:
            print("Accion: Inyectando presion a la red.")
            presion += 0.5
        elif presion >= 2.0 and presion <= 4.5:
            print("Accion: flujo nominal estabilizado")
            presion += 0.1
        else:
            print("Accion: purga de emergencia abierta")
            presion -= 0.8

verificar_presion(3.0)
verificar_presion(6.0)
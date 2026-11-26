while monitoreo:
   if nivel == 0 or nivel == 100:
         print("ERROR: Falla de lectura del sensor")
         monitoreo = False
   elif nivel < 15:
         print("Control: Bomba encendida - Nivel bajo")
         nivel += 5
   elif nivel >= 15 and nivel <= 85:
         print("Control: Operación hidráulica normal")
         nivel += 2
   else:
         print("Control: Bomba apagada - Tanque lleno")
         nivel -= 4

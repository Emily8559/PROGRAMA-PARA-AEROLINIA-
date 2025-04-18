class Persona:
    def __init__(self, nombre, edad, genero):
        self.__nombre = nombre
        self.__edad = edad
        self.__genero = genero.lower()
        
        
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_genero(self):
        return self.__genero
        
class Pasajero(Persona):
    def __init__(self, nombre, edad, genero, costo_tiquete):
        super().__init__(nombre, edad, genero)
        self.__costo_tiquete = costo_tiquete
        self.__equipaje = 0
        self.biciclata = 0
        self.gato = 0
        self.perro = 0
        
    def set_equipaje(self,peso):
        if peso >= 0:
            self.__equipaje = peso
    def get_equipaje(self):
        return self.__equipaje
    def get_costo_tiquete(self):
        return self.__costo_tiquete
    
    
    def calcular_costo_cargaEspecial(self):
    
        costo = self.biciclata * 7000  
        costo += self.gato * (self.__costo_tiquete * 0.02) 
        costo += self.perro * (self.__costo_tiquete * 0.05)  
        return costo
        
        
    def pasajero_infante(self):
        
        if self.get_edad() <= 13:
            return self.__costo_tiquete * 0.93  
        return self.__costo_tiquete  
    
    def costo_total(self):
        
        return self.pasajero_infante() + self.calcular_costo_cargaEspecial() + self.calcular_equipajeExtra()
    
    def registro_carga(self, biciclata, gato, perro, peso):
        self.__equipaje = peso
        self.biciclata = biciclata
        self.perro = perro
        self.gato = gato
        
        
class ClaseEconomica(Pasajero):
    def __init__(self, nombre, edad, genero, costo_tiquete):
        super().__init__(nombre, edad, genero, costo_tiquete)
        
        
    def calcular_equipajeExtra(self):
            if self.get_equipaje() > 10:
                return (self.get_equipaje() - 10) * 5000 
            return 0

class ClaseEjecutiva(Pasajero):
    def __init__(self, nombre, edad, genero, costo_tiquete):
        super().__init__(nombre, edad, genero, costo_tiquete)
        
    def calcular_equipajeExtra(self):
            if self.get_equipaje() > 20:
                return (self.get_equipaje() - 20) * 10000 
            return 0

class ClasePremium(Pasajero):
    def __init__(self, nombre, edad, genero, costo_tiquete):
        super().__init__(nombre, edad, genero, costo_tiquete)
    def calcular_equipajeExtra(self):
            if self.get_equipaje() > 30:
                excedente = self.get_equipaje() - 30
                return excedente * (0.01 * self.get_costo_tiquete())  
            return 0

class Vuelo:
    def __init__(self, c_origen, c_destino, fecha, hora):
        self.ciudad_origen = c_origen
        self.ciudad_destino = c_destino
        self.fecha = fecha
        self.hora = hora
        self.pasajeros = []
        self.tiquetes_recaudados = 0
        self.equipaje_recaudado = 0

        
    def agregar_pasajero(self, Pasajero):
        self.pasajeros.append(Pasajero)
        
        self.tiquetes_recaudados += Pasajero.pasajero_infante()
        
    def vender_tquete(self, pasajero):
        self.pasajeros.append(pasajero)
        
        self.tiquetes_recaudados += pasajero.pasajero_infante()
        
    def checkIN(self):
        for pasajero in self.pasajeros:
           
            self.equipaje_recaudado += pasajero.calcular_equipajeExtra() + pasajero.calcular_costo_cargaEspecial()
            
    def devolucion_tiquete(self, nombre):
        for pasajero in self.pasajeros:
            if pasajero.get_nombre() == nombre:
              
                self.tiquetes_recaudados -= pasajero.pasajero_infante()
                self.equipaje_recaudado -= (pasajero.calcular_equipajeExtra() + pasajero.calcular_costo_cargaEspecial())
                self.pasajeros.remove(pasajero)
                break
    
    def total_pasajeros(self):
        return len(self.pasajeros)
    
    def prom_costo(self):
        if self.pasajeros:
            return self.tiquetes_recaudados / len(self.pasajeros)
        return 0
    
    def genero_viajodestino(self):
        hombres = 0
        mujeres = 0
        for pasajero in self.pasajeros:
            if pasajero.get_genero().lower() == 'm':
                hombres += 1
            elif pasajero.get_genero().lower() == 'f':  
                mujeres += 1   
        return (hombres, mujeres)       
    
    def ingresos_vuelo_totales(self):
        
        return self.tiquetes_recaudados + self.equipaje_recaudado
    
class Aerolinia:
    def __init__(self):
        self.vuelos = []
        
    def crear_vuelo(self, c_origen, c_destino, fecha, hora): 
        vuelo = Vuelo(c_origen, c_destino, fecha, hora)
        self.vuelos.append(vuelo) 
        
    def hallar_uvuelo(self, c_origen, c_destino):
        for vuelo in self.vuelos:
            if vuelo.ciudad_origen == c_origen and vuelo.ciudad_destino == c_destino:
                return vuelo
        return None
    
    def trayecto_qmas_recaudo(self):
        mas_recaudo = 0
        vuelo_mas_recaudo = None
        for vuelo in self.vuelos:
            total = vuelo.ingresos_vuelo_totales()  
            if total > mas_recaudo:
                mas_recaudo = total
                vuelo_mas_recaudo = vuelo 
        return vuelo_mas_recaudo
    
    def comparar_genero_por_trayecto(self):
        resultado = []
        for vuelo in self.vuelos:
            hombres, mujeres = vuelo.genero_viajodestino()
            trayecto = f"{vuelo.ciudad_origen} - {vuelo.ciudad_destino}"
            if hombres > mujeres:
                resultado.append((trayecto, 'Hombres', hombres, mujeres))
            elif mujeres > hombres:
                resultado.append((trayecto, 'Mujeres', mujeres, hombres))
            else:
                resultado.append((trayecto, 'Ambos', hombres, mujeres))
        return resultado
    
    def Recaudototal_concepto_tiquetes(self):
        suma = 0 
        for vuelo in self.vuelos:
            suma += vuelo.tiquetes_recaudados
        return suma
    
    def Recaudototal_concepto_equipaje(self):
        suma = 0
        for vuelo in self.vuelos:
            suma += vuelo.equipaje_recaudado
        return suma
    
    def genero_viajodestin_end(self, vuelo):
        print(f'Costo promedio: ${vuelo.prom_costo():,.0f}')
        hombres, mujeres = vuelo.genero_viajodestino()
        print(f'Hombres: {hombres}, Mujeres: {mujeres}')
    
def menu():
    aerolinea = Aerolinia()

    while True:
        print("\n--- MENÚ ---")
        print("1. Crear vuelo")
        print("2. Vender tiquete")
        print("3. Hacer check-in")
        print("4. Devolver tiquete")
        print("5. Reportes de la aerolínea")
        print("6. Salir")

        try:
            opcion = input("Elige una opción: ")
            
            if opcion not in ["1", "2", "3", "4", "5", "6"]:
                raise ValueError("Opción no válida. Por favor ingrese un número del 1 al 6")

            if opcion == "1":
                try:
                    origen = input("Ciudad de origen: ")
                    destino = input("Ciudad de destino: ")
                    if not origen or not destino:
                        raise ValueError("Las ciudades de origen y destino no pueden estar vacías")
                    
                    fecha = input("Fecha del vuelo (formato DD/MM/AAAA): ")
                    hora = input("Hora del vuelo (formato HH:MM): ")
                    
                    vuelo = Vuelo(origen, destino, fecha, hora)
                    aerolinea.vuelos.append(vuelo)
                    print("Vuelo creado con éxito.")
                
                except Exception as e:
                    print(f"Error al crear vuelo: {str(e)}")

            elif opcion == "2":
                try:
                    origen = input("Ciudad de origen del vuelo: ")
                    destino = input("Ciudad de destino del vuelo: ")
                    vuelo = aerolinea.hallar_uvuelo(origen, destino)
                    
                    if not vuelo:
                        print("No se encontró el vuelo.")
                        continue
                        
                    nombre = input("Nombre del pasajero: ")
                    if not nombre:
                        raise ValueError("El nombre no puede estar vacío")
                        
                    edad = int(input("Edad: "))
                    if edad <= 0:
                        raise ValueError("La edad debe ser un número positivo")
                        
                    genero = input("Género (M/F): ").upper()
                    if genero not in ["M", "F"]:
                        raise ValueError("Género debe ser M o F")

                    print("Seleccione clase:")
                    print("1. Económica")
                    print("2. Ejecutiva")
                    print("3. Premium")
                    clase = input("Opción: ")

                    if clase not in ["1", "2", "3"]:
                        raise ValueError("Clase inválida")
                    
                    costo = 1500000 if clase == "1" else (2000000 if clase == "2" else 3500000)
                    
                    if clase == "1":
                        pasajero = ClaseEconomica(nombre, edad, genero, costo)
                    elif clase == "2":
                        pasajero = ClaseEjecutiva(nombre, edad, genero, costo)
                    else:
                        pasajero = ClasePremium(nombre, edad, genero, costo)

                    try:
                        peso = float(input("Peso del equipaje (kg): "))
                        if peso < 0:
                            raise ValueError("El peso no puede ser negativo")
                            
                        bici = int(input("¿Cuántas bicicletas?: "))
                        if bici < 0:
                            raise ValueError("La cantidad no puede ser negativa")
                            
                        perro = int(input("¿Cuántos perros?: "))
                        if perro < 0:
                            raise ValueError("La cantidad no puede ser negativa")
                            
                        gato = int(input("¿Cuántos gatos?: "))
                        if gato < 0:
                            raise ValueError("La cantidad no puede ser negativa")
                            
                    except ValueError as e:
                        print(f"Error en datos numéricos: {str(e)}")
                        continue

                    pasajero.registro_carga(bici, gato, perro, peso)
                    vuelo.agregar_pasajero(pasajero)

                    print(f"Tiquete vendido por ${pasajero.costo_total():,.0f}")

                except ValueError as e:
                    print(f"Error en los datos ingresados: {str(e)}")
                except Exception as e:
                    print(f"Error inesperado al vender tiquete: {str(e)}")

            elif opcion == "3":
                try:
                    origen = input("Ciudad de origen del vuelo: ")
                    destino = input("Ciudad de destino del vuelo: ")
                    vuelo = aerolinea.hallar_uvuelo(origen, destino)
                    
                    if not vuelo:
                        print("No se encontró el vuelo.")
                        continue
                        
                    vuelo.checkIN()
                    print("Check-in completado.")
                    print(f"Total recaudado por equipaje y cargas especiales: ${vuelo.equipaje_recaudado:,.0f}")
                
                except Exception as e:
                    print(f"Error al hacer check-in: {str(e)}")

            elif opcion == "4":
                try:
                    origen = input("Ciudad de origen del vuelo: ")
                    destino = input("Ciudad de destino del vuelo: ")
                    vuelo = aerolinea.hallar_uvuelo(origen, destino)
                    
                    if not vuelo:
                        print("No se encontró el vuelo.")
                        continue
                        
                    nombre = input("Nombre del pasajero a devolver: ")
                    
                    encontrado = False
                    for p in vuelo.pasajeros:
                        if p.get_nombre() == nombre:
                            print(f"Reembolsando ${p.costo_total():,.0f}")
                            encontrado = True
                            break
                    
                    if not encontrado:
                        print("Pasajero no encontrado en este vuelo")
                        continue
                        
                    vuelo.devolucion_tiquete(nombre)
                    print("Devolución realizada.")
                
                except Exception as e:
                    print(f"Error al devolver tiquete: {str(e)}")

            elif opcion == "5":
                try:
                    print("\n--- INFORME ---")
                    
                    # Trayecto con más recaudo
                    vuelo_max = aerolinea.trayecto_qmas_recaudo()
                    if vuelo_max:
                        print(f"\n1. Trayecto con más recaudo: {vuelo_max.ciudad_origen} - {vuelo_max.ciudad_destino}")
                        print(f"   Total recaudado: ${vuelo_max.ingresos_vuelo_totales():,.0f}")
                        print(f"   - Tiquetes: ${vuelo_max.tiquetes_recaudados:,.0f}")
                        print(f"   - Equipaje/cargas: ${vuelo_max.equipaje_recaudado:,.0f}")
                    else:
                        print("\nNo hay vuelos registrados")
                    
                    # Comparación de género
                    print("\n2. Comparación de género por trayecto:")
                    comparaciones = aerolinea.comparar_genero_por_trayecto()
                    if comparaciones:
                        for trayecto, genero_ganador, cantidad_mayor, cantidad_menor in comparaciones:
                            print(f"   {trayecto}: {genero_ganador} ({cantidad_mayor} --- {cantidad_menor})")
                    else:
                        print("   No hay datos de pasajeros")
                    
                    # Recaudos totales
                    print("\n3. Recaudos totales:")
                    tiquetes = aerolinea.Recaudototal_concepto_tiquetes()
                    equipaje = aerolinea.Recaudototal_concepto_equipaje()
                    print(f"   - Por tiquetes: ${tiquetes:,.0f}")
                    print(f"   - Por equipaje/cargas: ${equipaje:,.0f}")
                    print(f"   - Total general: ${tiquetes + equipaje:,.0f}")
                    
                    # Estadísticas por vuelo específico
                    print("\n4. Estadísticas por vuelo:")
                    origen = input("   Ciudad de origen (deje vacío para omitir): ")
                    if origen:
                        destino = input("   Ciudad de destino: ")
                        vuelo = aerolinea.hallar_uvuelo(origen, destino)
                        if vuelo:
                            print(f"\n   Estadísticas para {origen} - {destino}:")
                            print(f"   - Pasajeros totales: {vuelo.total_pasajeros()}")
                            print(f"   - Costo promedio tiquete: ${vuelo.prom_costo():,.0f}")
                            h, m = vuelo.genero_viajodestino()
                            print(f"   - Hombres: {h}, Mujeres: {m}")
                            print(f"   - Recaudo total: ${vuelo.ingresos_vuelo_totales():,.0f}")
                        else:
                            print("   Vuelo no encontrado.")
                
                except Exception as e:
                    print(f"Error al generar reportes: {str(e)}")

            elif opcion == "6":
                print("Gracias por usar el sistema.")
                break

        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    menu()






    
    

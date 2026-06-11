import csv

# =========================
# MOSTRAR PAÍS (FORMATEADO)
# =========================
def mostrar_pais(p):
    print(f"{p['nombre']:<15} | {p['poblacion']:<12} | {p['superficie']:<10} | {p['continente']}")

def mostrar_lista(paises):
    print("\nNombre          | Población    | Superficie | Continente")
    print("-" * 60)
    for p in paises:
        mostrar_pais(p)


# =========================
# CARGAR DATOS DESDE CSV
# =========================Argentina

def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }
                    paises.append(pais)
                except:
                    print("Error en formato de datos")
    except FileNotFoundError:
        print("Archivo no encontrado")
    
    return paises


# =========================
# AGREGAR PAÍS
# =========================
def agregar_pais(paises):
    nombre = input("Nombre: ").strip()
    continente = input("Continente: ").strip()

    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie: "))
    except:
        print("Datos inválidos")
        return

    if nombre == "" or continente == "":
        print("No se permiten campos vacíos")
        return

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })

    print("País agregado correctamente")


# =========================
# ACTUALIZAR PAÍS
# =========================
def actualizar_pais(paises):
    nombre = input("Ingrese el país a actualizar: ").lower()

    for pais in paises:
        if pais["nombre"].lower() == nombre:
            try:
                pais["poblacion"] = int(input("Nueva población: "))
                pais["superficie"] = int(input("Nueva superficie: "))
                print("Actualizado correctamente")
            except:
                print("Datos inválidos")
            return

    print("País no encontrado")


# =========================
# BUSCAR PAÍS
# =========================
def buscar_pais(paises):
    texto = input("Buscar: ").lower()
    resultados = [p for p in paises if texto in p["nombre"].lower()]

    if resultados:
        mostrar_lista(resultados)
    else:
        print("No se encontraron resultados")


# =========================
# FILTRAR
# =========================
def filtrar(paises):
    print("1. Continente")
    print("2. Rango población")
    print("3. Rango superficie")
    opcion = input("Elegir: ")

    if opcion == "1":
        cont = input("Continente: ").lower()
        resultado = [p for p in paises if p["continente"].lower() == cont]

    elif opcion == "2":
        try:
            min_p = int(input("Mínimo: "))
            max_p = int(input("Máximo: "))
            resultado = [p for p in paises if min_p <= p["poblacion"] <= max_p]
        except:
            print("Error")
            return

    elif opcion == "3":
        try:
            min_s = int(input("Mínimo: "))
            max_s = int(input("Máximo: "))
            resultado = [p for p in paises if min_s <= p["superficie"] <= max_s]
        except:
            print("Error")
            return
    else:
        print("Opción inválida")
        return

    if resultado:
        mostrar_lista(resultado)
    else:
        print("Sin resultados")


# =========================
# ORDENAR
# =========================
def ordenar(paises):
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    opcion = input("Elegir: ")

    reverse = input("Descendente? (s/n): ").lower() == "s"

    if opcion == "1":
        clave = "nombre"
    elif opcion == "2":
        clave = "poblacion"
    elif opcion == "3":
        clave = "superficie"
    else:
        print("Opción inválida")
        return

    ordenados = sorted(paises, key=lambda x: x[clave], reverse=reverse)
    mostrar_lista(ordenados)


# =========================
# ESTADÍSTICAS
# =========================
def estadisticas(paises):
    if not paises:
        print("No hay datos")
        return

    mayor = max(paises, key=lambda x: x["poblacion"])
    menor = min(paises, key=lambda x: x["poblacion"])

    promedio_pob = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_sup = sum(p["superficie"] for p in paises) / len(paises)

    continentes = {}
    for p in paises:
        cont = p["continente"]
        continentes[cont] = continentes.get(cont, 0) + 1

    print("\n--- ESTADÍSTICAS ---")
    print(f"Mayor población: {mayor['nombre']}")
    print(f"Menor población: {menor['nombre']}")
    print(f"Promedio población: {promedio_pob:.2f}")
    print(f"Promedio superficie: {promedio_sup:.2f}")
    print("Países por continente:")
    
    for cont, cantidad in continentes.items():
        print(f"{cont}: {cantidad}")


# =========================
# MENÚ PRINCIPAL
# =========================
def menu():
    paises = cargar_paises("paises.csv")

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar")
        print("5. Ordenar")
        print("6. Estadísticas")
        print("0. Salir")

        opcion = input("Elegir opción: ")

        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar(paises)
        elif opcion == "5":
            ordenar(paises)
        elif opcion == "6":
            estadisticas(paises)
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


menu()
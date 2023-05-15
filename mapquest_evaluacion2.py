import requests

url = "http://www.mapquestapi.com/directions/v2/route"

token = "4eaAz8Pb8zMberrCPCfdrMxpz3TvNhTi"

def obtener_distancia_duracion(origen, destino):
    params = {
        "key": token, "from": origen, "to": destino, "unit": "k", }

    response = requests.get(url, params=params)
    data = response.json()

    distancia = data["route"]["distance"]
    duracion = data["route"]["formattedTime"]
    instrucciones = data["route"]["legs"][0]["maneuvers"]

    return distancia, duracion, instrucciones

def imprimir_narrativa(distancia, duracion, instrucciones):
    print(f"Distancia del viaje: {distancia:.2f} km")
    print(f"Duración estimada: {duracion}")
    print("---------------------------------------------------------------------")
    print("\nNarrativa del viaje:")

    for i, instruccion in enumerate(instrucciones, 1):
        distancia = instruccion["distance"]
        calle = instruccion["narrative"]
        print(f"{i}. Avanza {distancia:.2f} metros por {calle}.")

print("\n---------------------------------------------------------------------")
origen = input("Ciudad de Origen: ")
destino = input("Ciudad de Destino: ")
print("--------------------------------------------------------------------")

distancia, duracion, instrucciones = obtener_distancia_duracion(origen, destino)
imprimir_narrativa(distancia, duracion, instrucciones)

print("\n---------------------------------------------------------------------")
salida = input("\nPresione 'q' para salir: ")

from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    # Convertir grados a radianes
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Diferencia de latitud y longitud
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula de Haversine
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Radio de la Tierra en kilómetros (aproximado)
    radius = 6371.0

    # Calcular la distancia
    distance = radius * c

    return distance

# Ejemplo de uso
lat1, lon1 = 40.7128, -74.0060  # Coordenadas de Nueva York
lat2, lon2 = 34.0522, -118.2437  # Coordenadas de Los Ángeles

result = haversine(lat1, lon1, lat2, lon2)
print(f"La distancia entre las dos coordenadas es: {result:.2f} km")

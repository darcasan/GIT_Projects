import requests as req
import matplotlib.pyplot as plt
import json

url = "https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/301aed82-339b-4005-ab20-06db41ee7017/download/municipio_comunidad_madrid.json"

res = req.get(url).json()
data = res["data"]
with open("data.json", "w", encoding="utf8") as file:
    json.dump(res, file, ensure_ascii=False, indent=4)

def get_ine (mun_ine):
    for mun in data:
        if mun ["municipio_codigo_ine"] == mun_ine:
            return mun

print(get_ine("280783"))

def get_biggest():
    big_area = 0.0
    biggest_mun = None
    for mun in data:
        if mun["superficie_km2"] >= big_area:
            big_area = mun["superficie_km2"]
            biggest_mun = mun["municipio_nombre"]
    return biggest_mun

biggest = get_biggest()
print(f"El municipio más grande es {biggest}")

def total_param(param):
    return sum(mun[param] for mun in data)

sup_total = total_param("superficie_km2")
den_total = total_param("densidad_por_km2")

print(f"La superficie total es {sup_total} km2")
print(f"La densidad total es {den_total} por km2")
    
def get_popu(mun_to_get):
    for mun in data:
        if mun["municipio_nombre"] == mun_to_get:
            return mun["superficie_km2"]*mun["densidad_por_km2"]

madrid = get_popu("Madrid ")
print (f"La población de Madrid es {madrid}")

pop_total = total_param("superficie_km2")*total_param("densidad_por_km2")
print(f"La poblacion media de los municipios es {pop_total/len(data)}")

def benford():
    result = {str(k):0 for k in range(1,10)}
    for mun in data:
        density = str(mun["densidad_por_km2"])
        result[density[0]] += 100/len(data)
    return result

print(benford())

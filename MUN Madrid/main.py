from unittest import result
import requests as req
import matplotlib.pyplot as plt
import json

url = "https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/301aed82-339b-4005-ab20-06db41ee7017/download/municipio_comunidad_madrid.json"

res = req.get(url).json() # dict key data: [list]:[dict]
data = res["data"]
with open("data.json", "w", encoding="utf8") as file:
    json.dump(res, file, ensure_ascii=False, indent=4)

def get_by_ine(mun_ine, dataset):
    for mun in dataset:
        if mun["municipio_codigo_ine"] == mun_ine:
            return mun

def get_bigger_than(sup):
    return filter(lambda mun: mun["superficie_km2"] >= sup,data)

get_bigger_than(100)

def get_bigger_than_2(sup):
    result = []
    for mun in data:
        if mun["superficie_km2"] >= sup:
            result.append(mun)
    return result

def get_biggest():
    biggest_mun = None
    top_area = 0.0
    for mun in data:
        if mun["superficie_km2"] >= top_area:
            top_area = mun["superficie_km2"]
            biggest_mun = mun
    return biggest_mun

def get_key(mun):
    return mun["densidad_por_km2"]

print(sorted(data, reverse=True, key=get_key)[0:5])

# print(get_biggest())

# eliminar a madrid del data

# superficie

def get_total(param):
    return sum([mun[param] for mun in data])
area_total = get_total("superficie_km2")
density_total = get_total("densidad_por_km2")
# population = area_total * density_total
# avg_population = population/len(data)

def popu_func():
    result = 0
    for mun in data:
        result += mun["superficie_km2"] * mun["densidad_por_km2"]
    return result

print(popu_func())
# print(sum(map(lambda mun: mun["superficie_km2"] * mun["densidad_por_km2"],data)))
# print(popu_func()/len(data))

# result = 0
# for mun in data:
#     result += mun["superficie_km2"]

def benford(data):
    result = {str(k):0 for k in range(1,10)}
    result = {}
    for num in range(1,10):
        result[str(num)] = 0
    for mun in data:
        density = str(mun["densidad_por_km2"])
        result[density[0]] += 100/len(data)
    return result




# NO PODEMOS ACTUALIZAR CLAVES INEXISTENTES
# ASIGNAR VALORES A CLAVES INEXISTENTES
def benford_2(data):
    result = {}
    for mun in data:
        first_digit = str(mun["densidad_por_km2"])[0]
        try:
            result[first_digit] += 100/len(data)
        except KeyError:
            result[first_digit] = 100/len(data)
    return result

def benford_3(data):
    result = {}
    for mun in data:
        first_digit = str(mun["densidad_por_km2"])[0]
        if result.get(first_digit):
            result[first_digit] += 100/len(data)
        else:
            result[first_digit] = 100/len(data)
    return result




# benford_list = benford(data)
# fig, ax = plt.subplots()

# ax.bar(range(1,10), benford_list.values(), width=1, edgecolor="white", linewidth=0.7)

# plt.show()
# plt.savefig("plot.png")
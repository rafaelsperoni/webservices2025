import json

with open("json/cursos.json") as json_file:
    dados = json.load(json_file)
    print(dados)

    print(type(dados))

    print(len(dados))

for item in dados:
    print(f"{item['nome']} - Coord: {item['coordenador']}")
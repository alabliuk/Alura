# Bibliotecas
import re
import urllib.request, json
import urllib.parse
import pandas
import Util

# Conexão ao servidor na Digital Ocean
cliente_MongoDB = Util.fnc_Conecta_Base_Documentos('<<usuario>>', '<<senha>>', '<< ip >>', '<<porta>>', 'dbclima')
db = cliente_MongoDB.dbclima

# Localizar último documento gravado
pipeline = [{ "$group": { "_id": "$posicao", "ultimo": { "$max": "$posicao" } } }]
consulta_ultimo_armazenado = db.clima.aggregate( pipeline )
obj = next(consulta_ultimo_armazenado, None)
ultimo_carregado = obj['ultimo']

# Leitura planilha com cidades, locais e datas
cidades = pandas.read_csv("Cidades_Datas_Distintas.csv")

# Indexando para facilitar a busca
cidades_indx =cidades.set_index("Id")

# Começa a iteração (apenas 10 linhas serão visitadas)
corrente = ultimo_carregado + 1
while (corrente <= ultimo_carregado + 10):
    estado =  cidades_indx.loc[corrente, "State"]
    cidade = cidades_indx.loc[corrente, "City"]
    data = cidades_indx.loc[corrente, "Sight_Date"]
    cabecalho = {
        'posicao': corrente,
        'estado': estado,
        'cidade': cidade
    }
    lugar = "http://api.wunderground.com/api/<< chave >>/history_" + str(data) + "/q/" + estado + "/" + cidade + ".json"

    # Trocando espaço por underscore:
    lugar = re.sub(" ", "_", lugar)
 
    # Antes de queimar um acesso ao website, conferir se "posicao" já não foi gravada
    consulta_corrente = db.clima.find({"posicao": corrente})
    if (consulta_corrente.count() == 0): # não achou

        # Acesso ao web site. Estamos limitados a 500 por dia e 10 por minuto
        try:
            with urllib.request.urlopen(lugar) as url:
                dados_web_site= json.loads(url.read().decode())

            # Juntando ambas as estruturas (dictionaries):
            json_para_gravar = {**cabecalho, **dados_web_site}

            # Inserindo documento na coleção "clima"
            resultado = db.clima.insert_one(json_para_gravar)
            print (corrente, estado, cidade, data)
        except:
            print ("Provavelmente inexiste cidade: " + cidade)
    else:
        print ("Documento existente!")
    corrente = corrente + 1
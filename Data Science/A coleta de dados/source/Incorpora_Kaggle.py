# Bibliotecas
import pandas
import Util
import re
import csv

# Montar data frame baseado em ufo.csv contendo ou forma ou cor ou ambos (colunas City, State e Time são mandatórias)
df_ufo = pandas.read_csv("D:\\Andre\\GitHub\\alabliuk\\Alura\\Data Science\\A coleta de dados\\data\\ufo.csv")

# Linhas contendo NaN nas colunas City, State ou Time devem ser eliminadas
df_ufo.dropna(axis=0, how='any', subset=['City','State', 'Time' ], inplace=True)
# Linhas contendo NaN em ambas colunas Colors Reported e Shape Reported devem ser eliminadas
df_ufo.dropna(axis=0, how='all', subset=['Colors Reported','Shape Reported'], inplace=True)

# Conexão:
cliente_MongoDB_db_clima = Util.fnc_Conecta_Base_Documentos('', '', '192.168.0.113', '27017', 'dbclima')
db_clima = cliente_MongoDB_db_clima.dbclima

# Inicia Caixa de Areia, destino das linhas cujos valores (cidade, estado, instante) não constam na base clima
caixa_de_areia = []

for index, row in df_ufo.iterrows():
    cidade = row["City"]
    estado = row["State"]
    instante = row["Time"]
    # Esmiuçando "Time" em: mês, dia, ano, hora e minuto. Exemplo de data: 8/21/2004 00:05
    # Temos que garantir o tamanho 2 para cada item.
    # Exemplo: se ler dia "8", precisamos transformá-lo em "08"
    # Para melhorar o percentual de busca, vamos desconsiderar minutos
    x = re.findall('\d+', instante) # Extraímos os 5 números
    mes = x[0].zfill(2)
    dia = x[1].zfill(2)
    ano = x[2].zfill(2)
    hora = x[3].zfill(2)
    #minuto = x[4].zfill(2)
    # Consulta
    anoint = int(ano)
    pipeline = [
            {"$match": { "estado" : estado, "cidade" : cidade }},
            {"$unwind": "$history.observations"},
            {"$match": {"history.observations.date.mon": mes,
                        "history.observations.date.mday": dia,
                        "history.observations.date.year": ano,
                        "history.observations.date.hour": hora,
                        # "history.observations.date.min": minuto,
                        }},
            {"$project": {"_id": 0,
                            "history.observations.tempi" : 1,
                            "history.observations.tempm" : 1,
                            "history.observations.dewptm" :1,
                            "history.observations.dewpti" : 1,
                            "history.observations.hum" : 1,
                            "history.observations.wspdm" : 1,
                            "history.observations.wspdi": 1,
                            "history.observations.wgustm": 1,
                            "history.observations.wgusti": 1,
                            "history.observations.wdird": 1,
                            "history.observations.wdire": 1,
                            "history.observations.vism": 1,
                            "history.observations.visi": 1,
                            "history.observations.pressurem": 1,
                            "history.observations.pressurei": 1,
                            "history.observations.windchillm": 1,
                            "history.observations.windchilli": 1,
                            "history.observations.heatindexm": 1,
                            "history.observations.heatindexi": 1,
                            "history.observations.precipm": 1,
                            "history.observations.precipi": 1,
                            "history.observations.conds": 1,
                            "history.observations.icon": 1,
                            "history.observations.fog": 1,
                            "history.observations.rain": 1,
                            "history.observations.snow": 1,
                            "history.observations.hail": 1,
                            "history.observations.thunder": 1,
                            "history.observations.tornado": 1
                            }}
                    ]
    busca_medida = db_clima.clima.aggregate(pipeline)
    medidas = next(busca_medida, None)
    if medidas:
        cabecalho = {
            'estado' : estado,
            'cidade' : cidade,
            'cor' : row["Colors Reported"],
            'formato' :row["Shape Reported"],
            'dia' : dia,
            'mes' : mes,
            'ano' : ano,
            'hora' : hora,
            # 'minuto' : minuto
        }
        # Juntando ambas as estruturas (dictionaries):
        json_para_gravar = {**cabecalho, **medidas}
        # Inserindo documento na coleção "clima"
        resultado = db_clima.clima_consolidado.insert_one(json_para_gravar)
        print (cidade, estado, ano, mes, dia, hora)
    else: #Não achou um registro com cidade/estado e instante. Mas nada impede que no futuro venha a achar
        print ('Não achou: ', cidade, estado, ano, mes, dia, hora,  ' -> Movendo para caixa de areia!')
        caixa_de_areia.append(row)
# Descarregando a caixa de areia
if caixa_de_areia:
    print ("-----------------------------Descarregando a Caixa de Areia!")
    f = open('D://Datasets//caixa_de_areia.csv', 'wt')
    try:
        writer = csv.writer(f)
        for i in caixa_de_areia:
            writer.writerow(i)
        print("-----------------------------Gerado arquivo caixa_de_areia.csv!")
    finally:
        f.close()
else:
    print ("-----------------------------Caixa de areia vazia!")

# Fim

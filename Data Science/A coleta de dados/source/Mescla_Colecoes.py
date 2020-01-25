# Bibliotecas
import Util
import re
import csv

# Temos duas coleções que precisam ser mescladas: ufo.ufos e dbclima.clima
# Para cada documento em dbclima.clima, vamos localizar cidade, estado, ano, mes, dia, hora e minuto em ufos.ufo
# Caso tenhamos um "match", um documento, mais enxuto, será gravado em uma terceira coleção
# Para os que não foram "casados", ainda existe esperança de fazê-lo no futuro

# Inicia Caixa de Areia, destino das linhas cujos valores (cidade, estado, instante) não constam na base clima
caixa_de_areia = []

# Conexões
cliente_MongoDB_ufos = Util.fnc_Conecta_Base_Documentos('', '', 'localhost', '27017', 'ufos')
db_ufos = cliente_MongoDB_ufos.ufos

cliente_MongoDB_db_clima = Util.fnc_Conecta_Base_Documentos('', '', 'localhost', '27017', 'dbclima')
db_clima = cliente_MongoDB_db_clima.dbclima

# Visitando todo documento da coleção de ufos
for u in db_ufos.ufo.find({}, { "_id" : 0, "City" : 1, "State" : 1, "Shape" : 1,
                                 "Sight_Year" : 1,"Sight_Month" : 1, "Sight_Day" : 1,
                                 "Sight_Time": 1}):
    cidade = u["City"]
    estado = u["State"]
    # Tratamento do ano. Teremos problemas em 2090!
    # Ideal seria mudar a fonte para que o ano venha com 4 dígitos
    ano = int(u["Sight_Year"])
    if ano > 90:
        ano = ano + 1900
    else:
        ano = ano + 2000
    ano = str(ano)

    mes = u["Sight_Month"].zfill(2)
    dia = u["Sight_Day"].zfill(2)
    # Esmiuçando "Sight_Time" em: hora e minuto. Exemplo  00:05
    # Temos que garantir o tamanho 2 para cada item.
    # Exemplo: se ler dia "8", precisamos transformá-lo em "08"
    x = re.findall('\d+', u["Sight_Time"]) # Extraímos os 2 números
    hora = x[0].zfill(2)
    #minuto = x[1].zfill(2)
    # Consulta
    pipeline = [
            {"$match": { "estado" : estado, "cidade" : cidade }},
            {"$unwind": "$history.observations"},
            {"$match": {"history.observations.date.mon": mes,
                        "history.observations.date.mday": dia,
                        "history.observations.date.year": ano,
                        "history.observations.date.hour": hora,
                        #"history.observations.date.min": minuto
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
    cabecalho = {
        'estado': estado,
        'cidade': cidade,
        'formato': u["Shape"],
        'dia': dia,
        'mes': mes,
        'ano': ano,
        'hora': hora
      #  'minuto': minuto
    }
    if medidas:
        # Juntando ambas as estruturas (dictionaries):
        json_para_gravar = {**cabecalho, **medidas}
        try:
            # Inserindo documento na coleção "clima"
            resultado = db_clima.clima_consolidado.insert_one(json_para_gravar)
            print (cidade, estado, ano, mes, dia, hora)
        except:
            print("Provavelmente tentativa de inseção duplicada: ", cidade, estado, ano, mes, dia, hora)
            caixa_de_areia.append(u)
    else: #Não achou um registro com cidade/estado e instante. Mas nada impede que no futuro venha a achar
        print ('Não achou: ', cidade, estado, ano, mes, dia, hora, ' -> Movendo para caixa de areia!')
        caixa_de_areia.append(estado + "-" + cidade + "-" + dia + "/" + mes + "/" + ano + ":" + hora)
# Descarregando a caixa de areia
if caixa_de_areia:
    print ("-----------------------------Descarregando a Caixa de Areia!")
    f = open('D://Datasets//caixa_de_areia_NUFORC.csv', 'wt')
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





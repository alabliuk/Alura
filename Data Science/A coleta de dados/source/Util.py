# Modulo contendo rotinas comuns

from pymongo import MongoClient
import urllib.parse

def fnc_Conecta_Base_Documentos (ent_usuario, ent_senha, ent_ender, ent_porta, ent_banco):
    if (ent_usuario == '' and ent_senha == ''):
        cliente_MongoDB = MongoClient('mongodb://%s:%s' % (ent_ender, ent_porta))
    else:
        usuario = urllib.parse.quote_plus(ent_usuario)
        senha = urllib.parse.quote_plus(ent_senha)
        cliente_MongoDB = MongoClient('mongodb://%s:%s@%s:%s/%s'% (usuario , senha , ent_ender, ent_porta, ent_banco))
    return cliente_MongoDB
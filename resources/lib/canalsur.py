# -*- coding: utf-8 -*-

"""CanalSur api"""

__author__ = "yeyus"

import logging
import requests
import json
from resources.lib.models import programa
from resources.lib.models import capitulo
from resources.lib.models import ultimo

CS_BASE = "https://www.canalsur.es/portal_rtva/app"
CS_LISTA_PROGRAMAS = "{}/programas_tv".format(CS_BASE)
CS_GET_PROGRAMA = "{}/programa_tv".format(CS_BASE) # id=idPrograma cat=categoria
CS_ULTIMOS = "{}/ultimos_tv".format(CS_BASE)
CS_DIRECTO = "http://iphone-andaluciatelevision.rtva.stream.flumotion.com/rtva/andaluciatelevision-iphone/main.m3u8"

def get_programas():
    #type: (None) -> List(Programa)
    r = requests.get(CS_LISTA_PROGRAMAS)
    programas = r.json()['programas']
    return map(lambda p: programa.from_json(p), programas)

def get_capitulos(id):
    #type: (int) -> List(Capitulo)
    r = requests.get(CS_GET_PROGRAMA, params={'id': id})
    capitulos = r.json()['listado']
    return map(lambda c: capitulo.from_json(c), capitulos)

def get_ultimos():
    #type: () -> List(Ultimo)
    r = requests.get(CS_ULTIMOS)
    ultimos = r.json()['ultimos']
    return map(lambda u: ultimo.from_json(u), ultimos)

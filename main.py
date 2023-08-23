# -*- coding: cp1252 -*-
import random

import paho.mqtt.client as paho
from paho import mqtt
from struct import pack
from random import randint
from time import sleep


# topicos providos por este sensor
ta = "D0-37-45-E8-58-3F/sensorTemperaturaAr"
ha = "D0-37-45-E8-58-3F/sensorHumidadeAr"
ts = "D0-37-45-E8-58-3F/sensorTemperaturaSolo"
hs = "D0-37-45-E8-58-3F/sensorHumidadeSolo"
l = "D0-37-45-E8-58-3F/sensorLuminosidade"
ph = "D0-37-45-E8-58-3F/sensorPh"
connect = "Connect"


client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)

# Habilita TLS para conexao segura
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# Define nome de usuario e senha
client.username_pw_set("thiago", "Thiago1234")
# Conecta ao HiveMQ Cloud na porta 8883 (padrao para MQTT)
client.connect("7179422ab76b4c6d8ecaa4a5dcfc530b.s2.eu.hivemq.cloud", 8883)

while True:
    # gera um valor de temperartura do ar aleatório
    rta = random.uniform(20, 25)
    payload = str(rta)
    # envia a publicação
    client.publish(ta, payload, qos=0)
    print(ta + "/" + payload)

    # gera um valor de umidade do ar aleatório
    rha = randint(80, 100)
    payload = str(rha)
    # envia a publicação
    client.publish(ha, payload, qos=0)
    print(ha + "/" + payload)

    # gera um valor de temperatura do solo aleatório
    rts = random.uniform(20, 25)
    payload = str(rts)
    # envia a publicação
    client.publish(ts, payload, qos=0)
    print(ts + "/" + payload)

    # gera um valor de umidade do solo aleatório
    rhs = randint(80, 100)
    payload = str(rhs)
    # envia a publicação
    client.publish(hs, payload, qos=0)
    print(hs + "/" + payload)

    # gera um valor de luminosidade aleatório
    rl = randint(0, 1023)
    payload = str(rl)
    # envia a publicação
    client.publish(l, payload, qos=0)
    print(l + "/" + payload)

    # gera um valor de ph aleatório
    rph = random.uniform(5, 9)
    payload = str(rph)
    # envia a publicação
    client.publish(ph, payload, qos=0)
    print(ph + "/" + payload)

    # Envia o Endereço MAC para fazer a conexão
    payload = "D0-37-45-E8-58-3F"
    # envia a publicação
    client.publish(connect, payload, qos=0)
    print(connect + "/" + payload)

    sleep(10)

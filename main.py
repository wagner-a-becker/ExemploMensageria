import time
import random
import paho.mqtt.client as paho
from paho import mqtt
from random import randint
from time import sleep
from datetime import datetime

# MAC fixo
mac = "B0:A7:32:15:00:CC"
# Configurando callbacks para diferentes eventos para verificar se eles funcionam e imprimir a mensagem, etc.
def on_connect(client, userdata, flags, rc, properties=None):
    """
        Imprime o resultado da conexao com um codigo de motivo no stdout (usado como callback para conectar)
        :param client: o proprio cliente
        :param userdata: userdata e definido ao iniciar o cliente, aqui e userdata=None
        :param flags: sao os flags de resposta enviados pelo broker
        :param rc: representa reasonCode, que e um codigo para o resultado da conexao
        :param properties: pode ser usado no MQTTv5, mas e opcional
    """
    print("CONNACK recebido com codigo %s." % rc)


# Com esse callback, voce pode ver se a publicacao foi bem-sucedida
def on_publish(client, userdata, mid, properties=None):
    """
        Imprime mid no stdout para garantir uma publicacao bem-sucedida (usado como callback para publicar)
        :param client: o proprio cliente
        :param userdata: userdata e definido ao iniciar o cliente, aqui e userdata=None
        :param mid: variavel retornada da chamada correspondente a publish(), para permitir o rastreamento de mensagens enviadas
        :param properties: pode ser usado no MQTTv5, mas e opcional
    """
    print("mid: " + str(mid))


# Imprime a qual topico foi inscrito
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    """
        Imprime uma confirmacao de inscricao bem-sucedida
        :param client: o proprio cliente
        :param userdata: userdata e definido ao iniciar o cliente, aqui e userdata=None
        :param mid: variavel retornada da chamada correspondente a publish(), para permitir o rastreamento de mensagens enviadas
        :param granted_qos: este e o qos que voce declara ao se inscrever, use o mesmo ao publicar
        :param properties: pode ser usado no MQTTv5, mas e opcional
    """
    print("Inscrito: " + str(mid) + " " + str(granted_qos))


# Imprime mensagem, util para verificar se foi bem-sucedido
def on_message(client, userdata, msg):
    """
        Imprime uma mensagem MQTT no stdout (usado como callback para se inscrever)
        :param client: o proprio cliente
        :param userdata: userdata e definido ao iniciar o cliente, aqui e userdata=None
        :param msg: a mensagem com topico e carga util
    """
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


# Usando a versao 5 do MQTT aqui, para 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata e um dado definido pelo usuario de qualquer tipo, atualizado por user_data_set()
# client_id e o nome dado ao cliente
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# Habilita TLS para conexao segura
#client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# Define nome de usuario e senha
client.username_pw_set("ClienteAPI", "#Api2023")
# Conecta ao HiveMQ Cloud na porta 8883 (padrao para MQTT)
client.connect('54.160.155.170', 1883)

# Configurando callbacks, use funcoes separadas como acima para melhor visibilidade
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# Inscreve em todos os topicos do esp32 usando o wildcard "#"
#client.subscribe("esp32/#", qos=1)
#client.subscribe("CONFIG/#", qos=1)
#client.subscribe("teste/topic", qos=1)

while True:
    # Obtém a data e hora do sistema
    current_time = datetime.now()
    date_time_str = current_time.strftime("%d-%m-%Y %H:%M:%S")

    # Gera um valor de temperatura do ar aleatório
    rta = random.uniform(20, 25)
    ta_topic = f"esp32/{mac}/{date_time_str}/RmTemperature"
    payload = str(rta)
    client.publish(ta_topic, payload, qos=0)
    print(ta_topic + "/" + payload)

    # Gera um valor de umidade do ar aleatório
    rha = randint(80, 100)
    ha_topic = f"esp32/{mac}/{date_time_str}/SilTemperature"
    payload = str(rha)
    client.publish(ha_topic, payload, qos=0)
    print(ha_topic + "/" + payload)

    # Gera um valor de temperatura do solo aleatório
    rts = random.uniform(20, 25)
    ts_topic = f"esp32/{mac}/{date_time_str}/SilHumidity"
    payload = str(rts)
    client.publish(ts_topic, payload, qos=0)
    print(ts_topic + "/" + payload)

    # Gera um valor de umidade do solo aleatório
    rhs = randint(80, 100)
    hs_topic = f"esp32/{mac}/{date_time_str}/AirHumidity"
    payload = str(rhs)
    client.publish(hs_topic, payload, qos=0)
    print(hs_topic + "/" + payload)


    # Gera um valor de luminosidade aleatório
    rl = randint(0, 1023)
    l_topic = f"esp32/{mac}/{date_time_str}/BatteryLevel"
    payload = str(rl)
    client.publish(l_topic, payload, qos=0)
    print(l_topic + "/" + payload)

    # Gera um valor de pH aleatório
    rph = random.uniform(5, 9)
    ph_topic = f"esp32/{mac}/{date_time_str}/PH"
    payload = str(rph)
    client.publish(ph_topic, payload, qos=0)
    print(ph_topic + "/" + payload)

    sleep(60)

# Uma unica publicacao, isso tambem pode ser feito em loops, etc.
#client.publish("esp32/working", payload="yes", qos=1)

# loop_forever para simplicidade, aqui voce precisa parar o loop manualmente
# voce tambem pode usar loop_start e loop_stop
#client.loop_forever()

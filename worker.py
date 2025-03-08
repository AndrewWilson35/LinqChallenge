from kafka import KafkaConsumer
from prometheus_client import start_http_server, Counter, Gauge

consumer = KafkaConsumer('quickstart-events',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='latest',
                         enable_auto_commit = False,
                         value_deserializer=lambda x: x.decode('utf-8'))
start_http_server(8000)

#Abbreviation is color sum counter (rsc = red sum counter)
rsc = Counter("RedCounter", "Sum of Red")
bsc = Counter("BlueCounter", "Sum of Blue")
gsc = Counter("GreenCounter", "Sum of Green")
ysc = Counter("YellowCounter", "Sum of Yellow")
psc = Counter("PurpleCounter", "Sum of Purple")
osc = Counter("OrangeCounter", "Sum of Orange")

numRed = 0
numBlue = 0
numGreen = 0
numYellow = 0
numPurple = 0
numOrange = 0

rgc = Gauge("RedGauge", "Average of Red")
bgc = Gauge("BlueGauge", "Average of Blue")
ggc = Gauge("GreenGauge", "Average of Green")
ygc = Gauge("YellowGauge", "Average of Yellow")
pgc = Gauge("PurpleGauge", "Average of Purple")
ogc = Gauge("OrangeGauge", "Average of Orange")

for msg in consumer:
    print(msg.timestamp, msg.value)
    tokens = msg.value.split()
    print(tokens)
    if tokens[2] == "Red":
        rsc.inc(int(tokens[4]))

    elif tokens[2] == "Blue":
        bsc.inc(int(tokens[4]))
    elif tokens[2] == "Green":
        gsc.inc(int(tokens[4]))
    elif tokens[2] == "Yellow":
        ysc.inc(int(tokens[4]))
    elif tokens[2] == "Purple":
        psc.inc(int(tokens[4]))
    else:
        osc.inc(int(tokens[4]))



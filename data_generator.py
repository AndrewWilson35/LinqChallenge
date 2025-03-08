from kafka import KafkaProducer
import random
import time

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
color = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]

while True:
    colorIndex = random.randint(0, 5)
    value = random.randint(0, 100)
    message = "{ Color: " + str(color[colorIndex]) + " Value: " + str(value) + " }"
    byteMessage = message.encode('utf-8')
    producer.send('quickstart-events', byteMessage)
    producer.flush()
    time.sleep(1)
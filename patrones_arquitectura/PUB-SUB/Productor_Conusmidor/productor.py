" Clase Productor "

from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers='localhost:9092')

producer.send('first_topic', key=b"100", value=b"desde python de nuevo")
producer.send('first_topic', key=b"200", value=b"Hola, para todos!")

producer.close()




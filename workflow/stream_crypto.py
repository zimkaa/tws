import time
import requests

from confluent_kafka import Producer

import config


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(
            f'Message delivered to {msg.topic()} [{msg.partition()}]',
        )


def main():
    while True:
        answer = requests.get(config.URL, headers=config.HEADERS)

        print(answer.text)

        producer = Producer({'bootstrap.servers': f'{config.HOST}:9092'})

        producer.produce(
            'events', answer.text.encode(), callback=delivery_report,
        )
        producer.flush()
        time.sleep(0.5)


if __name__ == "__main__":
    main()

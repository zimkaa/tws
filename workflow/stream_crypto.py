import json
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
        answer = requests.get(config.URL_GECKO, headers=config.HEADERS)
        time_stamp = time.time()
        print(f"time_stamp {time_stamp}")

        producer = Producer({'bootstrap.servers': f'{config.HOST}:9092'})

        data = json.loads(answer.text)

        for key in data.keys():
            write_data = json.dumps(
                {'name': key, 'price': data[key]['usd'], 'ts': time_stamp},
            )

            producer.produce(
                'events', write_data.encode(), callback=delivery_report,
            )
            producer.flush()

        time.sleep(1.5)


if __name__ == "__main__":
    main()

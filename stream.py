import asyncio

from confluent_kafka import Producer
import tinvest as ti

import config


async def main():
    async with ti.Streaming(config.TG_AP) as streaming:
        await streaming.candle.subscribe(
            'BBG0013HGFT4', ti.CandleResolution.min3,
        )
        producer = Producer({'bootstrap.servers': 'localhost:9092'})

        def delivery_report(err, msg):
            """ Called once for each message produced to indicate delivery result.
                Triggered by poll() or flush(). """
            if err is not None:
                print(f'Message delivery failed: {err}')
            else:
                print(
                    f'Message delivered to {msg.topic()} [{msg.partition()}]',
                )

        async for event in streaming:
            print(f"type {type(event)} event {event}")
            producer.produce(
                'registrations', str(event).encode(), callback=delivery_report,
            )
            producer.flush()


asyncio.run(main())

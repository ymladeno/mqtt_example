import logging
import asyncio
from operator import truediv
from amqtt.client import MQTTClient
from amqtt.mqtt.constants import QOS_1

logger = logging.getLogger(__name__)

class SystemManagerClient(MQTTClient):
    async def send_keep_active(self):
        logger.info("Send keep active")
        task = asyncio.create_task(self.publish("powerstate/keep_alive", b"active", qos=QOS_1))
        await task

async def main():
    formatter = "[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)

    client = SystemManagerClient()
    await client.connect("mqtt://localhost:1883")
    await client.send_keep_active()
    await client.disconnect()

asyncio.run(main())

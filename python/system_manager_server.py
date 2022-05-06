import logging
import asyncio
from amqtt.client import MQTTClient, ConnectException
from amqtt.mqtt.constants import QOS_1

logger = logging.getLogger(__name__)

class SystemManagerControl(MQTTClient): 
    async def get_keep_active(self):
        logger.info("enter get keep active")
        await super().subscribe(
            [
                ("powerstate/keep_alive", QOS_1)
            ]
        )
        logger.info("subscribed")
        message = await self.deliver_message()
        packet = message.publish_packet
        print(f"{packet.variable_header.topic_name} => {packet.payload.data}")

async def main():
    formater = (
        "[%(asctime)s] %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    )
    logging.basicConfig(level=logging.INFO, format=formater)

    controler = SystemManagerControl()
    await controler.connect(uri="mqtt://localhost:1883")
    await controler.get_keep_active()

asyncio.run(main())

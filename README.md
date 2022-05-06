## Starting mosquitto broker inside a docker container
cd ~/workspace/mosquitto-docker-compose/
docker run -it --name mosquitto -p 1883:1883 -v $(pwd)/config:/mosquitto/config/ eclipse-mosquitto /bin/sh
mosquitto -c mosquitto/config/mosquitto.conf &

## Subsribe for topic
mosquitto_sub -t 'test/topic' -v &

## Publish
mosquitto_pub -t 'test/topic' -m 'hello world'

## Starting mosquitto broker
docker-compose up -d

## Create conda environment
conda env create -f environment__ivs_car_system_test.yml

## Create server-client example
Server eill wait for keep active
Send back new state
Wait for acknowledge and send back again new state

Client will send keep active
Receive new state
Acknowledge new state

# Try amqtt - it does not work
amqtt
amqtt_sub --url mqtt://localhost:1883 -t test/#
amqtt_pub --url mqtt://localhost:1883 -t test -m "hi"

# Next 
To configure mosquitto broker to work not with localhost

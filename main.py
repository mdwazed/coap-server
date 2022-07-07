import asyncio
import base64
import datetime
import logging
import os.path
import time
import sys

import aiocoap
import aiocoap.resource as resource
from google.protobuf.json_format import MessageToDict

from protobuf import proto_config_pb2
from protobuf import proto_device_info_pb2
from protobuf import proto_measurements_pb2


# # Enter your database host, database user, database password and database name
# DATABASE_HOST = 'localhost'
# DATABASE_USER = 'riajulkashem'
# DATABASE_PASSWORD = 'password'
# DATABASE_NAME = 'iot_db'
# DATABASE_PORT = '5432'
#
# # Making the initial connection:
# conn = psycopg2.connect(
#     dbname=DATABASE_NAME,
#     user=DATABASE_USER,
#     host=DATABASE_HOST,
#     password=DATABASE_PASSWORD,
#     port=DATABASE_PORT
# )


# Measurements - Class used to handle Measurement messages sent by the sensor
class Measurements(resource.Resource):

    def __init__(self):
        super().__init__()

    async def render_post(self, request):

        logging.info(f'received request for measurements')
        # Creating a dictionary from a received message.
        data = [MessageToDict(proto_measurements_pb2.ProtoMeasurements().FromString(request.payload))]
        logging.info(f'received payload data: {data}')
        ser_num = data[0]['serialNum']
        logging.info(f'Serial num: {ser_num}')
        record = []
        changeAt = []
        # Set request_device_info to true
        device_config = proto_config_pb2.ProtoConfig()
        
        device_config.request_device_info = True
        device_config.request_configuration = True
        device_config.transmission_interval = 60

        if ser_num == 'KCwCQOZz':
            logging.info(f'Changing transmission interval for KCwCQOZz')
            device_config.transmission_interval = 60
        # Serializing device config.
        response_payload = device_config.SerializeToString()

        # iteration in list data
        for measurement in data:

            for param in measurement['channels']:

                # iteration in list data/measurement/channels/sampleOffsets.
                # Creating a list of sensor parameters(measured_at,serial_number, battery_status)
                # and measurement results with sample offset

                if param != {}:
                    if param['type'] == "MEASUREMENT_TYPE_OK_ALARM":
                        numberOfMeasurements = 1 + (abs(param['sampleOffsets'][-1]) - 1) / measurement[
                            'measurementPeriodBase']
                        for sampleOffset in param['sampleOffsets']:
                            timeDifference = measurement['measurementPeriodBase'] * int(
                                (abs(sampleOffset - 1) / measurement['measurementPeriodBase']))
                            if sampleOffset > 0:
                                changeAt.extend([param['timestamp'] + timeDifference, "Alarm"])
                            elif sampleOffset < 1:
                                changeAt.extend([param['timestamp'] + timeDifference, "OK"])
                        for measurementNumber in range(int(numberOfMeasurements)):
                            timeDifference = measurement['measurementPeriodBase'] * measurementNumber
                            if param['timestamp'] + timeDifference in changeAt:
                                value = changeAt[changeAt.index(param['timestamp'] + timeDifference) + 1]
                            record.extend([(datetime.datetime.fromtimestamp(param['timestamp'] + timeDifference),
                                            base64.b64decode((measurement['serialNum'])).hex(),
                                            measurement['batteryStatus'],
                                            param['type'].replace("MEASUREMENT_TYPE_", ""), value)])
                    else:
                        for sampleOffset in param['sampleOffsets']:
                            if param['type'] == "MEASUREMENT_TYPE_TEMPERATURE" or param[
                                'type'] == "MEASUREMENT_TYPE_ATMOSPHERIC_PRESSURE":
                                value = (param['startPoint'] + sampleOffset) / 10
                            else:
                                value = param['startPoint'] + sampleOffset
                            timeDifference = measurement['measurementPeriodBase'] * param['sampleOffsets'].index(
                                sampleOffset)
                            record.extend([(datetime.datetime.fromtimestamp(param['timestamp'] + timeDifference),
                                            base64.b64decode((measurement['serialNum'])).hex(),
                                            measurement['batteryStatus'],
                                            param['type'].replace("MEASUREMENT_TYPE_", ""),
                                            value)])

                # measurements = "INSERT INTO measurements(measured_at, serial_number, battery_ok, type, value) VALUES (%s, %s, %s, %s, %s)"
                # with conn.cursor() as cur:
                #     try:
                #         # inserting a list of sensor parameters and measurement to table in PostgresSQL
                #         cur.executemany(measurements, record)
                #         conn.commit()
                #         cur.close()
                #     except (Exception, psycopg2.DatabaseError) as error:
                #         print(error)
        # returning "ACK" and response payload to the sensor
        
        resp_msg = aiocoap.Message(mtype=aiocoap.ACK, code=aiocoap.Code.CREATED,
                               token=request.token, payload=response_payload)
        logging.info(f'response msg: {resp_msg}')
        return resp_msg


# DeviceInfo - Class used to handle Device Info messages sent by the sensor
class DeviceInfo(resource.Resource):

    def __init__(self):
        super().__init__()

    async def render_post(self, request):
        logging.info(f'received post request for device info')
        # Creating a dictionary from a message received from a sensor
        data = [MessageToDict(proto_device_info_pb2.ProtoDeviceInfo().FromString(request.payload))]
        logging.info(f'data: {data}')
        # Create the file "Deviceinfo.txt" and save the date in this file
        if not os.path.isfile("Deviceinfo.txt"):
            file = open("Deviceinfo.txt", 'x')
        else:
            file = open("Deviceinfo.txt", 'w')
        file.write(str(data))
        file.close()
        # returning "ACK" to the sensor
        return aiocoap.Message(mtype=aiocoap.ACK, code=aiocoap.Code.CREATED,
                               token=request.token, payload="")


# Configuration - Class used to handle Configuration messages sent by the sensor
class Configuration(resource.Resource):

    def __init__(self):
        super().__init__()

    async def render_post(self, request):
        logging.info(f'received post request for configuration')
        # Creating a dictionary from a message received from a sensor
        data = [MessageToDict(proto_config_pb2.ProtoConfig().FromString(request.payload))]
        logging.info(f'data: {data}')
        # Create the file "Configuration.txt" and save the date in this file
        if not os.path.isfile("Configuration.txt"):
            file = open("Configuration.txt", 'x')
        else:
            file = open("Configuration.txt", 'w')
        file.write(str(data))
        file.close()
        # returning "ACK" to the sensor
        return aiocoap.Message(mtype=aiocoap.ACK, code=aiocoap.Code.CREATED,
                               token=request.token, payload="")


# Time - Class used to handle Time messages sent by the sensor
class Time(resource.Resource):

    def __init__(self):
        super().__init__()

    async def render_post(self, request):
        logging.info(f'received request for time')
        time_stamp = int(time.time())
        time_stamp_hex = hex(time_stamp)

        # returning timestamp to the sensor
        return aiocoap.Message(mtype=aiocoap.ACK, code=aiocoap.Code.CREATED,
                               token=request.token, payload=bytearray.fromhex(time_stamp_hex[2:]))


async def main():
    logging.basicConfig(filename='coap_server.log', encoding='utf-8', level=logging.DEBUG, 
                        format='%(asctime)s %(message)s')
    # Resource tree creation
    root = resource.Site()
    # Set up “m” endpoint, which will be receiving measurements sent by Efento NB-IoT sensor using POST method
    root.add_resource(["m"], Measurements())
    # Set up “i” endpoint, which will be receiving device info messages sent by Efento NB-IoT sensor using POST method
    root.add_resource(["i"], DeviceInfo())
    # Set up “c” endpoint, which will be receiving configuration messages sent by Efento NB-IoT sensor using POST method
    root.add_resource(["c"], Configuration())
    # Set up “t” endpoint, which will be receiving time sent by Efento NB-IoT sensor using POST method
    root.add_resource(["t"], Time())

    # Starting the application on set IP address and port.
    logging.info('Creating server in port 5683')
    await aiocoap.Context.create_server_context(root, ('0.0.0.0', 5683))
    # Getting the current event loop and create an asyncio.Future object attached to the event loop.
    await asyncio.get_running_loop().create_future()


if __name__ == '__main__':
    # Run the coroutine, taking care of managing the asyncio event loop,
    asyncio.run(main())

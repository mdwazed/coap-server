import asyncio

from aiocoap import *
from main import Measurements
from protobuf import proto_measurements_pb2


async def main():
    context = await Context.create_client_context()

    msg = proto_measurements_pb2.ProtoMeasurements()
    msg.serial_num = b'12345'
    msg.battery_status = True


    payload = msg.SerializeToString()

    # request = Message(code=POST, payload=payload, uri="coap://3.74.88.33/m")
    req_msg = Message(code=POST, payload=payload, uri="coap://127.0.0.1/m")
    
    print('sending req')
    response = await context.request(req_msg).response
    print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
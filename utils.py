from protobuf import proto_config_pb2

def update_config(id):
    device_config = proto_config_pb2.ProtoConfig()
    device_config.request_device_info = True
    device_config.request_configuration = True
    device_config.transmission_interval = 180
    response_payload = device_config.SerializeToString()

import grpc
import time

# placeholder imports — Monad protobufs
# from monad.node_pb2 import StatusRequest
# from monad.node_pb2_rpc import NodeStub

class MonadRPCClient:
    def __init__(self, endpoint="localhost:9090"):
        self.endpoint = endpoint

    def collect(self):
        # NOTE: here intentionally lightweight and safe
        data = {
            "rpc_reachable": False,
            "block_height": None,
            "syncing": None,
            "timestamp": time.time()
        }

        try:
            channel = grpc.insecure_channel(self.endpoint)
            grpc.channel_ready_future(channel).result(timeout=2)

            # stub = NodeStub(channel)
            # status = stub.Status(StatusRequest())

            # mocked values until proto binding
            data["rpc_reachable"] = True
            data["block_height"] = 123456
            data["syncing"] = False

        except Exception as e:
            data["error"] = str(e)

        return data

import psutil
from metrics.rpc_client import MonadRPCClient

class RuntimeMetrics:
    def __init__(self):
        self.start_peers = self.peers()
        self.rpc = MonadRPCClient()

    def peers(self):
        return len(psutil.net_connections())

    def finish(self, duration):
        end_peers = self.peers()
        grpc_metrics = self.rpc.collect()

        data = {
            "duration_sec": round(duration, 2),
            "peers_before": self.start_peers,
            "peers_after": end_peers,
            "rpc": rpc_metrics
        }

        print("[METRICS]", data)
        return data

import subprocess, os

class PacketLoss:
    def apply(self, params):
        loss = params.get("percent", 5)
        if os.getenv("DRY_RUN") == "1":
            print(f"[DRY] tc loss {loss}%")
            return
        subprocess.run(
            ["tc","qdisc","add","dev","eth0","root","netem","loss",f"{loss}%"],
            check=True
        )

    def rollback(self):
        if os.getenv("DRY_RUN") == "1":
            return
        subprocess.run(["tc","qdisc","del","dev","eth0","root"], check=True)

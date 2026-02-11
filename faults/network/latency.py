import subprocess, os

class NetworkLatency:
    def apply(self, params):
        delay = params.get("delay_ms", 200)
        if os.getenv("DRY_RUN") == "1":
            print(f"[DRY] tc delay {delay}ms")
            return
        subprocess.run(
            ["tc","qdisc","add","dev","eth0","root","netem","delay",f"{delay}ms"],
            check=True
        )

    def rollback(self):
        if os.getenv("DRY_RUN") == "1":
            return
        subprocess.run(["tc","qdisc","del","dev","eth0","root"], check=True)

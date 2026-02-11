import subprocess
import os
import signal

class ResourceStress:
    def __init__(self):
        self.proc = None

    def apply(self, params):
        cpu = params.get("cpu", 2)
        io = params.get("io", 1)
        timeout = params.get("timeout", 30)

        cmd = [
            "stress-ng",
            f"--cpu={cpu}",
            f"--io={io}",
            f"--timeout={timeout}s",
            "--metrics-brief"
        ]

        if os.getenv("DRY_RUN") == "1":
            print(f"[DRY] stress-ng cpu={cpu} io={io} timeout={timeout}s")
            return

        self.proc = subprocess.Popen(cmd)

    def rollback(self):
        if self.proc and self.proc.poll() is None:
            self.proc.send_signal(signal.SIGTERM)
            self.proc.wait()

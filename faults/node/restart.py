import subprocess, os

class NodeRestart:
    def apply(self, params):
        svc = params.get("service", "storyd")
        if os.getenv("DRY_RUN") == "1":
            print(f"[DRY] systemctl restart {svc}")
            return
        subprocess.run(["systemctl","restart",svc], check=True)

    def rollback(self):
        pass

import os

class Guardrails:
    def __init__(self, scenario):
        self.scenario = scenario

    def validate(self):
        if self.scenario.get("network") == "mainnet":
            os.environ["DRY_RUN"] = "1"
            print("[SAFE MODE] mainnet enforced")

        if os.getenv("DRY_RUN") is None:
            os.environ["DRY_RUN"] = "1"

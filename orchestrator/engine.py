import time
from faults.registry import FAULTS
from metrics.runtime import RuntimeMetrics
from reports.generate_report import generate_report

class ChaosEngine:
    def __init__(self, scenario):
        self.scenario = scenario
        self.metrics = RuntimeMetrics()

    def run(self):
        start = time.time()
        print(f"[+] Scenario: {self.scenario['scenario']}")

        for fault in self.scenario["faults"]:
            f = FAULTS[fault["type"]]
            print(f"[>] {fault['type']}")
            f.apply(fault.get("params", {}))
            time.sleep(fault.get("duration", 5))
            f.rollback()

        results = self.metrics.finish(time.time() - start)
        generate_report(self.scenario["scenario"], results)

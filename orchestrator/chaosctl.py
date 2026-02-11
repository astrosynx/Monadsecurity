import sys, yaml
from orchestrator.engine import ChaosEngine
from safety.guardrails import Guardrails

def main():
    if len(sys.argv) < 2:
        print("Usage: chaosctl <scenario.yaml>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        scenario = yaml.safe_load(f)

    Guardrails(scenario).validate()
    ChaosEngine(scenario).run()

if __name__ == "__main__":
    main()

from datetime import datetime
import json

def generate_report(name, metrics):
    with open("chaos_report.md", "w") as f:
        f.write(f"# Chaos Report\n\n")
        f.write(f"Scenario: {name}\n")
        f.write(f"Generated: {datetime.utcnow()} UTC\n\n")

        f.write("## Runtime\n")
        f.write(f"- Duration: {metrics['duration_sec']}s\n")
        f.write(f"- Peers before: {metrics['peers_before']}\n")
        f.write(f"- Peers after: {metrics['peers_after']}\n\n")

        f.write("## RPC Status\n")
        for k, v in metrics["rpc"].items():
            f.write(f"- {k}: {v}\n")

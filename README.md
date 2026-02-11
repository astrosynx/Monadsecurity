# 🚀 Astrosynx — Stress & Chaos Testing Suite

Production-oriented **chaos & stress testing toolkit** for **Monad validator nodes**.  
Designed to safely simulate real-world failure conditions, measure recovery behavior, and improve operational resilience **before incidents happen**.

---

## 🧠 What Is This?

Astrosynx Stress & Chaos Testing Suite is a **scenario-driven framework** that allows validator operators to deliberately introduce controlled failures into their infrastructure and observe how systems behave under pressure.

The goal is **not to break the network**, but to answer critical operational questions:

- How fast does a node recover after failure?
- Does it rejoin peers correctly?
- Are monitoring and alerting systems reacting in time?
- Which configurations degrade silently under load?

---

## ✨ Key Features

✅ Scenario-based fault injection (YAML)  
🌐 Network degradation (latency, packet loss)  
🔁 Validator service restarts (systemd)  
🔥 CPU & IO stress testing (`stress-ng`)  
📡 RPC-level Monad observability  
📊 Recovery & MTTR measurement  
🛡️ Safe-by-default execution (`DRY_RUN`)  
🧩 Modular & extensible architecture  

---

## 🧱 High-Level Architecture

```mermaid
flowchart TD
    %% =====================
    %% Operator Input
    %% =====================
    subgraph Input["Operator & Configuration"]
        A1["Validator Operator"]
        A2["Scenario YAML<br/>(faults, timing, params)"]
    end

    %% =====================
    %% Control Layer
    %% =====================
    subgraph Control["Control & Orchestration"]
        B1["CLI Controller<br/>(chaosctl.py)"]
        B2["Safety Guardrails<br/>(DRY_RUN, mainnet-safe)"]
        B3["Chaos Engine<br/>(fault sequencing)"]
    end

    %% =====================
    %% Fault Injection
    %% =====================
    subgraph Faults["Fault Injection Layer"]
        C1["Network Faults<br/>(tc / netem)"]
        C2["Node Faults<br/>(systemd restart)"]
        C3["Resource Stress<br/>(stress-ng CPU / IO)"]
    end

    %% =====================
    %% Runtime Environment
    %% =====================
    subgraph Runtime["Validator Runtime"]
        D1["Monad Validator Node"]
        D2["Host OS & Network Stack"]
    end

    %% =====================
    %% Observability
    %% =====================
    subgraph Metrics["Metrics & Observability"]
        E1["Runtime Metrics<br/>(duration, peers)"]
        E2["Monad RPC Metrics<br/>(health, sync, height)"]
    end

    %% =====================
    %% Reporting
    %% =====================
    subgraph Output["Reporting & Artifacts"]
        F1["Metrics Aggregation"]
        F2["Chaos Report<br/>(chaos_report.md)"]
    end

    %% =====================
    %% Data Flow
    %% =====================
    A1 --> A2
    A2 --> B1

    B1 --> B2 --> B3

    B3 --> C1
    B3 --> C2
    B3 --> C3

    C1 --> D2
    C2 --> D1
    C3 --> D2

    D1 --> E1
    D1 --> E2
    D2 --> E1

    E1 --> F1
    E2 --> F1

    F1 --> F2
```

---

## 💥 Fault Injection Types

### 🌐 Network Faults
- Artificial latency injection
- Packet loss simulation
- Connectivity degradation scenarios

### 🔁 Node Faults
- Controlled validator service restarts
- Recovery and resync behavior validation

### 🔥 Resource Pressure
- CPU saturation
- Disk / IO contention
- Combined stress scenarios via `stress-ng`

---

## 📊 Metrics Collected

📈 Execution duration  
🔗 Peer count before / after faults  
📡 gRPC reachability  
⛓️ Block height visibility  
🔄 Syncing status  
⏱️ Recovery behavior indicators  

These signals allow **direct correlation** between injected failures and actual protocol-level behavior.

---

## 🛡️ Safety Model

Safety is enforced at the framework level:

- 🧯 `DRY_RUN=1` enabled by default  
- 🚫 Mainnet → automatic safe-mode  
- 🔄 Explicit rollback for all faults  
- ⚠️ No cascading or parallel faults by default  

This makes the suite suitable for **real infrastructure testing** without unnecessary risk.

---

## 🧪 Example Scenario

```yaml
scenario: cpu_io_pressure
network: testnet

faults:
  - type: node.resource_stress
    duration: 30
    params:
      cpu: 4
      io: 2
      timeout: 30
```

---

## ⚙️ Installation

```bash
git clone https://github.com/astrosynx/chaos-suite
cd astrosynx-chaos-suite
pip install -r requirements.txt
```

### System dependencies

- `tc`
- `stress-ng`
- `systemd`

## ▶️ Usage

```bash
python orchestrator/chaosctl.py examples/network_latency.yaml
```

Dry-run mode is applied automatically unless explicitly disabled.

---

## 🧩 Typical Use Cases

- Validator resilience testing  
- Upgrade & restart validation  
- Monitoring and alerting verification  
- Infrastructure comparison  
- Operational readiness assessments  

---

## 🛣️ Roadmap

🔜 MTTR timelines & recovery graphs  
🔜 Missed block correlation  
🔜 Peer churn analytics  
🔜 Mainnet-safe fault profiles  
🔜 Cross-network support  

The framework is designed to **scale beyond Monad** and be adaptable to other blockchain networks.

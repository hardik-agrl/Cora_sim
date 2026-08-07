# CoRA: Confidential State Migration in Dynamic Sharded Blockchains

A lightweight research prototype implementing **CoRA (Confidential State Migration)**, a protocol for secure migration of confidential blockchain state across dynamic shards while preserving atomicity, replay protection, and bounded proof validity.

> **Research Prototype**
> This implementation accompanies an M.Tech thesis and is intended to validate the protocol logic presented in the research paper. It is not a production blockchain implementation.

---

## Overview

Dynamic sharding improves blockchain scalability by redistributing accounts between shards. Existing migration mechanisms mainly focus on plaintext account states, while confidential blockchain systems rely on commitments, nullifiers, and zero-knowledge proofs.

CoRA extends this model by enabling confidential state migration through an owner-authorized **spend-and-mint** protocol that preserves:

- Atomic cross-shard migration
- Commitment re-randomization
- Replay protection using nullifiers
- Bounded proof-validity continuity
- Owner-authorized migration

---

## Project Structure

```
cora_sim/
│
├── crypto/
│   ├── commitment.py
│   ├── nullifier.py
│   └── proof.py
│
├── shard/
│   ├── merkle_tree.py
│   ├── nullifier_set.py
│   ├── root_window.py
│   └── shard.py
│
├── protocol/
│   ├── owner.py
│   ├── relay.py
│   ├── redemption.py
│   └── timeout.py
│
├── simulation/
│   ├── network.py
│   ├── metrics.py
│   └── driver.py
│
├── experiments/
│
├── tests/
│
├── config.py
├── main.py
└── requirements.txt
```

---

## Protocol Workflow

```
Owner
   │
   ▼
Create Migration Transaction
   │
   ▼
Relay Verification
   │
   ├── Commitment Verification
   ├── Nullifier Check
   ├── Proof Verification
   ▼
Atomic Commit
   │
   ├── Spend Source Commitment
   └── Create Destination Commitment
   ▼
Migration Complete
```

---

## Implemented Components

### Cryptographic Layer

- Commitment generation
- Commitment re-randomization
- Nullifier generation
- Mock proof generation and verification

### Storage Layer

- Merkle tree
- Nullifier set
- Historical root window
- Shard abstraction

### Protocol Layer

- Owner-side migration transaction construction
- Cross-shard relay execution
- Bounded root verification
- Timeout handling

### Simulation

- End-to-end migration execution
- Success/failure metrics
- Latency measurement

---

## Current Status

Implemented:

- [x] Confidential commitment creation
- [x] Commitment re-randomization
- [x] Nullifier generation
- [x] Merkle-based shard storage
- [x] Cross-shard migration protocol
- [x] End-to-end simulator
- [x] Migration metrics

Planned:

- [ ] CSV result generation
- [ ] Replay attack simulation
- [ ] Timeout experiments
- [ ] Baseline comparison
- [ ] Publication-quality graphs

---

## Running the Simulator

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the simulator:

```bash
python main.py
```

Example output:

```
========== Simulation ==========
Transactions : 100
Successful   : 100
Failed       : 0
Success Rate : 100.00%
Avg Latency  : 122.85 ms
```

---

## Experimental Metrics

The simulator records:

- Total transactions
- Successful migrations
- Failed migrations
- Average migration latency
- Success rate

Future versions will include replay attacks, timeout analysis, and baseline comparisons.

---

## Scope

This implementation focuses on validating the **protocol behavior** rather than deploying a production blockchain.

The following components are intentionally simplified:

- Zero-knowledge proofs
- Consensus protocol
- Network communication
- Validator signatures

These components are represented by lightweight abstractions to isolate the protocol logic.

---

## Research

This project accompanies the research work:

**CoRA: Confidential State Migration and Commitment Re-Anchoring Across Dynamic Sharded Blockchains**

---

## License

This repository is intended for academic and research purposes.

# NovaPrototype Architecture v0

Date: 2026-08-26  
Owner: Esslinger & Co. · Hannover node

## Intent

NovaPrototype is the **public laboratory**, not the production orchestrator.

- Production / private orchestration stays in private hubs (`nexus-ecosystem`, `nova-nexus`, `lumiaos`).
- Anything that can be shown, forked and reproduced without leaking keys lives here.

## Layers

1. **Oracle layer** (`proto/`)  
   Physical or simulated sensors and actuators. Each folder is one experiment.

2. **Contract layer** (`core/`)  
   Shared Python interfaces so Soilnova, Vista Nova, Lumia and future oracles speak the same language.

3. **Agent layer** (`agents/`)  
   Thin adapters. Lumia / Lyra handle presence and affect; Xen handles diagnostics and scaling notes.

4. **Mesh hook** (optional, later)  
   Status payloads can be published onto NovaNet / QNET without embedding private peer keys in this repo.

## Graduation rule

When an experiment is stable for more than two lab cycles:

- extract it into its own repository
- leave a stub + link in `proto/`
- keep the shared contract in `core/`

## Non-goals for this repo

- Private Kyber material, live peer lists, token wallets
- Corporate / Delaware filings
- Full swarm runtime (that belongs to Lumia OS / Nexus orchestrator)

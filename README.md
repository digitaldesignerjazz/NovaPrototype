# NovaPrototype

**NovaPrototype** is the public sandbox of the Nexus prototype layer by Esslinger & Co.

It is the place for fast, reproducible experiments that later graduate into dedicated repos (Soilnova, Vista Nova, York Autotype, Lumia, Grok Launcher).

## Purpose

- Rapid iteration on hardware/software oracles that feed the Nexus stack
- Shared, public scaffolding so experiments stay cloneable and testable
- Clean hooks into mesh (NovaNet / xMesh / QNET / Yggdrasil), AI swarms (Lumia / Lyra / Xen / Elara) and incentives (XCoin / QCoin / NovaRune)

## Architecture (v0)

```
NovaPrototype
├── proto/          # isolated experiments (one folder per prototype)
├── core/           # shared interfaces: sensors, actuators, mesh hooks
├── agents/         # thin agent adapters for swarm control
├── scripts/        # local start / status / validate helpers
└── docs/           # architecture notes and lab logs
```

Each prototype in `proto/` should expose the same contract:

1. `README.md` — what it is and how to run it
2. `status()` — health + last reading
3. `tick()` — one iteration of the experiment loop
4. optional mesh / agent adapters under `core/` and `agents/`

## Status

Public bootstrap — 26 August 2026. First scaffold is `proto/hello-nova`.

## Related repositories

- [nexus](https://github.com/digitaldesignerjazz/nexus) — central integration hub
- [novanet](https://github.com/digitaldesignerjazz/novanet) — mesh initiative
- [lumina](https://github.com/digitaldesignerjazz/lumina) — lighting / display prototype
- [nova-os](https://github.com/digitaldesignerjazz/nova-os) — swarm OS
- [nexus-go](https://github.com/digitaldesignerjazz/nexus-go) — Go orchestrator

## Quick start

```bash
git clone https://github.com/digitaldesignerjazz/NovaPrototype.git
cd NovaPrototype
python3 proto/hello-nova/hello.py
```

## License

MIT — see `LICENSE`.

---

*Part of the Nexus Initiative — Esslinger & Co. · Hannover*

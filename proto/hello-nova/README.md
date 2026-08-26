# hello-nova

First public experiment in NovaPrototype.

## Run

```bash
python3 proto/hello-nova/hello.py
```

Expected output:

```
[hello-nova] healthy=True ticks=1
NovaPrototype public sandbox is live.
```

## Contract

Implements `core.contract.Prototype`:

- `status()` — always healthy, reports tick count and node `hannover`
- `tick()` — increments the counter and returns status

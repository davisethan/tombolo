# tombolo

Docker image that exposes R statistical methods over JSON-RPC 2.0.

```
docker pull ethandavisecd/tombolo:latest
```

The primary interface is the [tombolo Python package](https://pypi.org/project/tombolo/), which handles the Docker subprocess and protocol transparently. The sections below are for anyone calling the image directly.

## Protocol

Send a JSON-RPC 2.0 request on stdin. The result is written to stdout.

```json
{
  "jsonrpc": "2.0",
  "method": "nma",
  "params": {
    "data": [...],
    "greater_is_better": true
  },
  "id": 1
}
```

```
echo '<request>' | docker run --rm -i ethandavisecd/tombolo:latest
```

## Methods

See the [documentation](https://ethandavisecd.github.io/tombolo) for parameters and return values.

| Method | Description |
|--------|-------------|
| `nma`  | Frequentist random-effects network meta-analysis via `netmeta` |
| `bnma` | Bayesian random-effects network meta-analysis via `gemtc` and JAGS |

## License

MIT

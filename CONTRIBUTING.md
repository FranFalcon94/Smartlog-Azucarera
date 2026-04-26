# Contributing to SmartLog Azucarera

Thanks for taking the time to contribute.

## Scope

This is a small educational repo. Contributions are welcome if they:

- keep the core logger simple and readable
- improve reliability, documentation, or security posture
- add optional features behind clear switches (no hard dependencies for the CLI)

## Development setup

```powershell
cd smartlog-azucarera
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -U pip
py -m pip install -r requirements-dev.txt
```

## Running the logger

```powershell
py main.py
```

## Demo dashboard

```powershell
py -m pip install -r requirements-demo.txt
streamlit run streamlit_app.py
```

## API docs

Generate static HTML docs from docstrings:

```powershell
py -m pdoc -o site/api .
```

## Proposed roadmap

- Add a minimal CLI (`run`, `export`, `verify`) while preserving `main.py` as a simple entrypoint.
- Add integrity protection for backups (e.g., HMAC signature).
- Add data retention policy tooling (purge by age).
- Add a GitHub Actions workflow to publish `site/api` to GitHub Pages.

## Pull request checklist

- Documentation is updated (README and/or MANUAL).
- New behavior is described with a reproducible example.
- If you add dependencies, keep them in the optional `requirements-*.txt` files.

## Code of Conduct

By participating, you are expected to follow `CODE_OF_CONDUCT.md`.

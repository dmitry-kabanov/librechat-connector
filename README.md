# LibreChat Connector

Small Python app that automatically connects to a server which hosts
LibreChat and opens it in a web browser.

Right now the app uses its own browser (which is based on Chromium) to serve
the LibreChat's web page.

## Installation

1. Create a Conda environment:

```bash
conda create -n librechat-connector python=3.12
```

2. Activate the environment:

```bash
conda activate librechat-connector
```

3. Install the dependencies:

```bash
pip install PySide6 PySide6-Essentials
```

## How to run

```bash
python src/main.py
```

The app depends on the presence of the environment variable `LIBRECHAT_CONNECTOR_HOST`,
which specifies the hostname/IP-address of the server.

<h3 align="center">🛠️ privacy-pixel</h3>

<div align="center">
  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)  
[![Build Status](https://img.shields.io/badge/build-passing-success.svg)](#)  
[![Stars](https://img.shields.io/github/stars/your-org/privacy-pixel?style=social)](https://github.com/your-org/privacy-pixel)

</div>

---  

# 🚀 privacy-pixel  
**Power privacy‑conscious users with a zero‑knowledge, fully‑local image‑processing engine.**  
Edit, redact, and analyze pictures entirely in the browser – nothing ever leaves the client.

## Why privacy-pixel?

- **100 % Local Processing** – Every operation runs in‑browser, guaranteeing that no image data is transmitted or stored remotely.  
- **Zero‑Knowledge Architecture** – All edits are performed client‑side; the library never logs, caches, or telemeters any user content.  
- **Open‑Source Transparency** – Full source code is available under MIT, enabling audits and community contributions.  
- **Lightweight Footprint** – Only a few kilobytes of JavaScript/WASM are loaded, keeping page load times minimal.  
- **Easy Integration** – Drop‑in Python package for server‑side tooling or embed the compiled WASM bundle in any web stack.  
- **Built for Privacy‑First Apps** – Ideal for SaaS products, internal tools, or personal projects that must respect data sovereignty.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Client‑Side Redaction** | Paint, blur, or pixelate regions without ever sending the image to a server. |
| **Metadata Scrubbing** | Strip EXIF, GPS, and other identifying metadata locally. |
| **Format Conversion** | Convert between PNG, JPEG, WebP, and AVIF entirely in the browser. |
| **Batch Processing API** | Process multiple images in a single call with async support. |
| **Extensible Plugins** | Add custom filters or transformations via a simple plugin interface. |
| **Type‑Safe Python Wrapper** | Use the same engine from Python scripts for CI pipelines or offline tooling. |

## Tech Stack
The definitive stack is documented in **[decisions/tech-stack.md](decisions/tech-stack.md)**.  
*We intentionally keep this section aligned with the locked decisions file – no additional technologies are introduced here.*

## Project Structure

```
privacy-pixel/
├─ business/          # Business‑logic docs, BMC, PRD, etc.
├─ docs/              # Markdown documentation, ROADMAP, TECH_SPEC
├─ src/               # Core source code (Python + WASM bindings)
├─ tests/             # Unit and integration test suite
├─ README.md
├─ pyproject.toml     # Build system, entry points, dependencies
└─ requirements.txt   # Pin‑exact Python dependencies
```

## Getting Started

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-org/privacy-pixel.git
cd privacy-pixel

# 2️⃣ Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# 3️⃣ Install the package in editable mode
pip install -e .

# 4️⃣ Verify the installation
privacy-pixel --help
```

### Running the test suite

```bash
# Install test dependencies (already in requirements.txt)
pip install -r requirements.txt

# Execute tests
pytest -q
```

## Deploy

The project is a pure‑Python library with an optional WebAssembly bundle; deployment consists of publishing the package to PyPI or bundling the WASM for front‑end use.

```bash
# Build distribution artifacts
python -m build

# Publish to PyPI (requires proper credentials)
twine upload dist/*
```

For front‑end consumption, copy the generated `privacy_pixel.wasm` from `src/` into your static assets and load it via the provided JavaScript loader (see `docs/WEB_INTEGRATION.md`).

## Status
Active development – latest commit `7a40955` (2026‑06‑09) adds full documentation artifacts and stabilises the build pipeline.

## Contributing
We welcome contributions! Please read our **[CONTRIBUTING.md](CONTRIBUTING.md)** for guidelines on how to propose changes, run tests, and submit pull requests.

## License
This project is licensed under the **MIT License**.
<h3 align="center">🛠️ privacy-pixel</h3>

<div align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/language-Python%203.11-brightgreen.svg" alt="Language">
  <img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Build Status">
  <img src="https://img.shields.io/github/stars/axentx/privacy-pixel?style=social" alt="GitHub stars">
</div>

---

# 🚀 privacy-pixel

**Power privacy‑conscious developers with zero‑knowledge image editing.**  
A client‑side, 100 % local image editor that guarantees data sovereignty by never sending images to a server.

## Why privacy-pixel?

- **Zero‑knowledge**: All edits happen entirely in the browser – no telemetry, no backend storage.  
- **Local‑first**: Images never leave the user’s device, ensuring complete data sovereignty.  
- **Open‑source**: Transparent codebase with permissive MIT license.  
- **Fast**: Built on WebAssembly and optimized for low‑latency editing.  
- **Cross‑platform**: Works in any modern browser, no native app required.  
- **Built for**: Privacy‑first designers, journalists, and security teams who need to edit images without risking data leaks.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Client‑side rendering** | Uses WebGL for instant, high‑performance image manipulation. |
| **Zero‑knowledge architecture** | No telemetry, no backend – all data stays local. |
| **Multiple filter presets** | Built‑in filters (sepia, grayscale, HDR) and custom LUT support. |
| **Undo/redo stack** | Unlimited history with efficient memory usage. |
| **Export options** | JPEG, PNG, WebP with adjustable quality. |
| **Accessibility** | Keyboard shortcuts, screen‑reader friendly UI. |

## Tech Stack

*(See `decisions/tech-stack.md` for the definitive list.)*

- Python 3.11
- Pyodide (Python in WebAssembly)
- WebAssembly (WASM)
- HTML5 Canvas
- CSS3
- JavaScript (ES6+)

## Project Structure

```
privacy-pixel/
├── business/          # Business logic and configuration
├── src/               # Core library and WASM bindings
├── tests/             # Automated test suite
├── pyproject.toml     # Build and dependency configuration
└── README.md          # This file
```

## Getting Started

```bash
# Install dependencies
pip install -e .

# Run the development server
python -m privacy_pixel.dev

# Run tests
pytest tests/
```

## Deploy

```bash
# Build the WebAssembly package
python -m build

# Deploy to GitHub Pages (example)
gh-pages -d dist
```

## Status

Active development – last commit `f534e23` (2026‑06‑09 04:17:17 UTC) added the initial code‑build cycle.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT © Axentx
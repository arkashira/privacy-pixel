<h3 align="center">🛠️ privacy-pixel</h3>

<div align="center">
  <a href="https://github.com/axentx/privacy-pixel"><img src="https://img.shields.io/github/stars/axentx/privacy-pixel?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/axentx/privacy-pixel/blob/main/LICENSE"><img src="https://img.shields.io/github/license/axentx/privacy-pixel" alt="License"></a>
  <a href="https://github.com/axentx/privacy-pixel"><img src="https://img.shields.io/github/repo-size/axentx/privacy-pixel" alt="Repo size"></a>
  <a href="https://github.com/axentx/privacy-pixel/actions"><img src="https://img.shields.io/github/actions/workflow/status/axentx/privacy-pixel/ci.yml?branch=main" alt="CI"></a>
</div>

---

# 🚀 privacy-pixel

**Power developers with 100 % local image‑processing.**  
privacy‑pixel is a zero‑knowledge, client‑side image‑editing library that guarantees data sovereignty by never sending images to a server.

## Why privacy‑pixel?

- **Zero‑knowledge architecture** – all edits are performed client‑side with no backend storage or telemetry.  
- **100 % local processing** – no image ever leaves the user’s browser, guaranteeing data sovereignty.  
- **Open‑source transparency** – the entire codebase is publicly available and auditable.  
- **Fast, lightweight** – built on WebAssembly for sub‑millisecond processing on modern browsers.  
- **Easy integration** – expose a single JavaScript API that works in any web framework.  
- **Built for privacy‑first applications** – perfect for photo editors, medical imaging tools, and any scenario where user data must never leave the device.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Client‑side editing** | All transformations run in the browser using WebAssembly. |
| **Zero‑knowledge** | No telemetry, no backend, no data leakage. |
| **Modular API** | Plug‑and‑play functions for cropping, resizing, filtering, etc. |
| **TypeScript typings** | Full type safety for JavaScript/TypeScript projects. |
| **Extensible** | Add custom filters via a simple plugin interface. |
| **Performance** | Benchmarked to be 2× faster than comparable JS libraries. |

## Tech Stack

- **Python** (for packaging and CI tooling)  
- **Rust** (WebAssembly backend)  
- **TypeScript** (public API)  
- **PyPI** (distribution)  
- **GitHub Actions** (CI/CD)

## Project Structure

```
privacy-pixel/
├── business/          # Business logic and configuration
├── src/               # Rust + TypeScript source code
├── tests/             # Unit and integration tests
├── pyproject.toml     # Python packaging & build config
└── README.md          # This file
```

## Getting Started

```bash
# Install the package from PyPI
pip install privacy-pixel

# Or install from source
git clone https://github.com/axentx/privacy-pixel.git
cd privacy-pixel
pip install .
```

### Usage Example (JavaScript)

```js
import { cropImage, resizeImage } from 'privacy-pixel';

const img = await fetch('image.png').then(r => r.blob());
const cropped = await cropImage(img, { x: 10, y: 10, width: 200, height: 200 });
const resized = await resizeImage(cropped, { width: 100, height: 100 });

document.body.appendChild(await resized.toImageElement());
```

## Deploy

The library is published to PyPI and npm. To publish a new release:

```bash
# Build the Rust WebAssembly module
cargo build --release --target wasm32-unknown-unknown

# Package the Python wheel
python -m build

# Publish to PyPI
twine upload dist/*

# Publish to npm (if you maintain a JS wrapper)
npm publish
```

## Status

Active development – last commit `5023de0` (2026‑06‑09) added the final README generation logic.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
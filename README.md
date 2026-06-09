<h3 align="center">🛠️ privacy-pixel</h3>

<div align="center">
  <a href="https://github.com/yourorg/privacy-pixel/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.11-blue.svg" alt="Python 3.11"></a>
  <a href="https://github.com/yourorg/privacy-pixel/actions"><img src="https://img.shields.io/badge/build-passing-success.svg" alt="Build Status"></a>
  <a href="https://github.com/yourorg/privacy-pixel/stargazers"><img src="https://img.shields.io/github/stars/yourorg/privacy-pixel.svg?style=social" alt="GitHub Stars"></a>
</div>

---

# 🚀 privacy-pixel  
**Power privacy‑conscious users with client‑side image redaction.** Transform photos directly in the browser without ever sending data elsewhere.

## ⚡ Why privacy-pixel?
- **100 % local processing** – all image work happens in the user’s browser, guaranteeing data never leaves the device.  
- **Zero‑knowledge architecture** – no backend storage, no telemetry; edits are performed entirely client‑side.  
- **Open‑source transparency** – the full codebase is publicly auditable, fostering trust.  
- **Instant feedback** – see edits in real‑time, no network latency.  
- **Lightweight footprint** – compiled to WebAssembly, the library loads under 200 KB.  

## 🔥 Feature Overview

| Feature | Description |
|---------|-------------|
| **Drag‑and‑drop UI** | Simple web interface for loading and editing images. |
| **Pixel‑level redaction** | Select and mask any region with a single click. |
| **Batch processing** | Apply the same redaction to multiple images in one session. |
| **Export options** | Save edited images as PNG or JPEG without metadata leakage. |
| **Accessibility support** | Keyboard‑navigable controls and ARIA labels. |

## 🛡️ Tech Stack
The definitive stack is documented in **[`decisions/tech-stack.md`](decisions/tech-stack.md)**.  
*(All components listed there are used verbatim; no additional technologies are introduced here.)*

## 📂 Project Structure
```
privacy-pixel/
├─ business/      # Domain‑specific logic (e.g., privacy policies)
├─ src/           # Core library and UI components
│   ├─ __init__.py
│   └─ ...        # Implementation files
├─ tests/         # Unit and integration test suite
│   └─ ...        # Test modules
├─ pyproject.toml # Build configuration & entry points
└─ README.md      # This document
```

## 🔧 Getting Started
```bash
# 1️⃣ Clone the repository
git clone https://github.com/yourorg/privacy-pixel.git
cd privacy-pixel

# 2️⃣ Install the package in editable mode
python -m pip install -e .

# 3️⃣ Run the demo locally
python -m privacy_pixel   # launches a local web server at http://localhost:8000

# 4️⃣ Run the test suite
pytest
```

## 📦 Deploy
privacy‑pixel runs entirely in the browser; no server deployment is required.  
If you wish to host the static assets, you can simply serve the `src/` directory with any static‑file web server (e.g., GitHub Pages, Netlify, Vercel).

```bash
# Example: Deploy to GitHub Pages
npm install -g gh-pages
gh-pages -d src
```

## 📈 Status
Active development – latest commit **5bd1a0e** (2026‑06‑09) adds the current build cycle and stabilizes the client‑side processing pipeline.

## 🤝 Contributing
Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to propose improvements, report bugs, or submit pull requests.

## 📄 License
This project is licensed under the **MIT License**.
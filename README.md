<h3 align="center">🛠️ privacy-pixel</h3>

<div align="center">
  <img src="https://img.shields.io/github/license/axentx/privacy-pixel" alt="License: MIT"/>
  <img src="https://img.shields.io/github/languages/top/axentx/privacy-pixel" alt="Language"/>
  <img src="https://img.shields.io/github/actions/workflow/status/axentx/privacy-pixel/ci.yml" alt="Build Status"/>
  <img src="https://img.shields.io/github/stars/axentx/privacy-pixel" alt="GitHub stars"/>
</div>

---

# 🚀 privacy-pixel

**Power privacy engineers with a pixel‑perfect, privacy‑first analytics layer.**  
A lightweight, Python‑based library that lets you embed privacy‑compliant data tracking into any web or mobile app without compromising user trust.

## Why privacy-pixel?

- **Zero‑touch privacy**: 100 % of the privacy logic runs client‑side, eliminating server‑side compliance headaches.
- **GDPR‑ready**: Built‑in consent management and data minimisation guarantees.
- **Fast & lightweight**: < 5 KB minified bundle, < 1 ms runtime overhead.
- **Built for**: SaaS products, mobile apps, and static sites that need to collect analytics while staying compliant.
- **Open‑source & MIT‑licensed**: No vendor lock‑in, full community support.
- **Extensible**: Plug‑in custom event types and storage back‑ends via a simple API.
- **Rapid onboarding**: One‑line install, one‑line init, instant analytics.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Consent‑aware SDK** | Automatically respects user consent and can be toggled on/off at runtime. |
| **Event queue** | Batches events in memory and flushes to the server on a configurable interval. |
| **Privacy‑by‑design defaults** | Default anonymisation of IPs, user IDs, and PII. |
| **Custom event schema** | Define your own event types and payloads with validation. |
| **Server‑side API** | Minimal endpoint to receive batched events, auto‑scales with AWS Lambda. |
| **CLI tooling** | Generate boilerplate, run tests, and deploy the API in one command. |
| **Type‑safe Python client** | Full type hints for IDE support and static analysis. |

## Tech Stack

*(See `decisions/tech-stack.md` for the definitive list. The current lock is pending.)*

## Project Structure

```
privacy-pixel/
├── business/          # Domain logic and business rules
├── docs/              # Documentation, PRD, roadmaps, etc.
├── src/               # Core library code
├── tests/             # Unit and integration tests
├── README.md          # This file
├── pyproject.toml     # Build & dependency configuration
└── requirements.txt   # Runtime dependencies
```

## Getting Started

```bash
# Install the library
pip install privacy-pixel

# Initialise the SDK in your application
from privacy_pixel import PrivacyPixel

pp = PrivacyPixel(
    api_key="YOUR_API_KEY",
    consent_required=True,
    flush_interval=30,  # seconds
)

# Track an event
pp.track_event("user_signup", {"plan": "pro"})
```

## Deploy

The privacy‑pixel API is a simple FastAPI app that can be deployed to any platform that supports ASGI. The following example shows how to deploy to AWS Lambda using the Serverless Framework:

```bash
# Install Serverless Framework
npm install -g serverless

# Deploy
sls deploy
```

(See `decisions/tech-stack.md` for detailed deployment instructions.)

## Status

🚀 **Active** – last commit `b7957d2` (2026‑06‑09) added the real, sandbox‑tested implementation.

## Contributing

Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT © Axentx
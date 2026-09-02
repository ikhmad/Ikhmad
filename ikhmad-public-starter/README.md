# IKHMAD

**Wildfire Intelligence, Coordination & Evacuation Platform**

> Current status: High-fidelity product prototype / pre-MVP.

IKHMAD is a wildfire intelligence and emergency coordination platform designed to connect citizens, operators, geospatial data, alerts, incident workflows and future predictive evacuation capabilities in one system.

This public repository documents the product direction, public architecture, API contracts, sample data models and demonstration code. It intentionally does **not** contain the proprietary decision logic, calibrated risk models, source-reliability rules, predictive hazard implementation or confidential production infrastructure.

## Product vision

IKHMAD aims to support the full emergency chain:

**Detection → Reporting → Verification → Risk assessment → Alerting → Coordination → Evacuation → Continuous reassessment**

The platform is designed around two main user surfaces:

- **Citizen application** — incident reporting, alerts, risk awareness, SOS, evacuation guidance and safety information.
- **Command-center dashboard** — incident review, validation, operational map, reports, alerts, response coordination and future decision-support tools.

## Current prototype

The current product prototype demonstrates:

- citizen onboarding and location-aware home experience;
- wildfire map and incident details;
- citizen fire reporting;
- incident status / verification flow;
- emergency alerts;
- SOS workflow;
- evacuation guidance and safe-zone experience;
- dynamic rerouting concept;
- professional command-center incident management;
- citizen ↔ operator workflow concept.

> The current prototype demonstrates intended system behavior. Production backend integrations and proprietary intelligence engines are part of the staged MVP roadmap.

## Public architecture

```text
 Citizens                         Operators
    |                                |
    v                                v
Mobile App                    Command Dashboard
      \                            /
       \                          /
             Public API Layer
                   |
       +-----------+-----------+
       |           |           |
       v           v           v
   Incidents     Alerts        SOS
       |
       v
+--------------------------------------+
|       IKHMAD INTELLIGENCE LAYER      |
|          Proprietary Core            |
+--------------------------------------+
       |
+------+----------------------+---------+
|                             |         |
v                             v         v
GIS / Geospatial          Routing    Safe Zones
Services                  Interface   Interface
       |
       v
   Data Platform
       |
+------+----------+-----------+--------+
|                 |           |        |
v                 v           v        v
Satellite      Weather    Road/GIS   Other Sources
```

## Repository scope

### Included publicly

- product and system overview;
- public architecture;
- citizen and command-center workflows;
- API interface contracts;
- basic public data models;
- synthetic examples;
- demonstration / mock code;
- roadmap;
- security and privacy principles.

### Intentionally not included

- incident confidence formulas;
- calibrated thresholds;
- source-reliability scoring;
- wildfire hazard prediction internals;
- predictive evacuation algorithm internals;
- future-road traversability calculations;
- safe-zone scoring logic;
- anti-fraud / false-report models;
- private datasets and calibration data;
- production credentials or infrastructure secrets.

These components belong to IKHMAD's confidential / proprietary technology layer and may be subject to future trade-secret and/or patent protection.

## Repository structure

```text
ikhmad/
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── COPYRIGHT.md
├── SECURITY.md
├── docs/
│   ├── PRODUCT_OVERVIEW.md
│   ├── ARCHITECTURE.md
│   ├── CITIZEN_WORKFLOW.md
│   ├── COMMAND_CENTER_WORKFLOW.md
│   ├── INCIDENT_LIFECYCLE.md
│   ├── EVACUATION_OVERVIEW.md
│   ├── DATA_SOURCES.md
│   ├── SECURITY_PRIVACY.md
│   ├── IP_BOUNDARY.md
│   └── ROADMAP.md
├── api/
│   └── openapi-public.yaml
├── examples/
│   ├── incident-example.json
│   ├── alert-example.json
│   ├── sos-example.json
│   └── evacuation-example.json
└── demo/
    ├── package.json
    └── src/
        ├── models.js
        └── simulation.js
```

## Development status legend

Throughout this repository:

- ✅ **Implemented / demonstrated**
- 🟡 **Prototype / mocked**
- ⏳ **Planned**
- 🔒 **Proprietary / private**

## Roadmap snapshot

| Phase | Scope | Status |
|---|---|---|
| Phase 0 | High-fidelity citizen + command-center prototype | ✅ |
| Phase 1 | Connected MVP: auth, incident API, SOS, alerts, realtime events | ⏳ |
| Phase 2 | Multi-source incident intelligence + external data integration | ⏳ |
| Phase 3 | Predictive evacuation + dynamic hazard-aware routing | ⏳ |
| Phase 4 | Institutional pilot + field validation | ⏳ |

See [`docs/ROADMAP.md`](docs/ROADMAP.md).

## Intellectual property

IKHMAD's brand, original software, documentation, visual assets and proprietary technology are intended to remain controlled by the project/company.

This repository is public for transparency, technical communication and development history. Publication of a file here does not mean that all IKHMAD technology has been disclosed.

See [`COPYRIGHT.md`](COPYRIGHT.md) and [`docs/IP_BOUNDARY.md`](docs/IP_BOUNDARY.md).

## Security

Never commit:

- API keys;
- passwords;
- private keys;
- production URLs with embedded credentials;
- personal emergency data;
- real citizen location histories;
- confidential institutional data.

See [`SECURITY.md`](SECURITY.md).

## Contact

Project: **IKHMAD**

Status: Prototype / pre-MVP

Copyright © 2026 IKHMAD. All rights reserved.

# Public Architecture

This document describes IKHMAD at a system-boundary level. Proprietary decision-making internals are intentionally excluded.

## Client layer

### Citizen mobile application
Responsible for:
- authentication/session;
- location permission;
- map presentation;
- incident report submission;
- alert presentation;
- SOS initiation;
- evacuation UI;
- offline/degraded-state behavior.

### Command-center dashboard
Responsible for:
- incident queue;
- map view;
- incoming report review;
- validation/state changes;
- alerts;
- SOS monitoring;
- operational status;
- future decision-support presentation.

## API layer

The public API surface is organized around:
- incidents;
- reports;
- alerts;
- SOS;
- hazards;
- routes;
- safe zones.

See `api/openapi-public.yaml`.

## Intelligence layer

The following logical services are part of IKHMAD's proprietary core:

- incident confidence / corroboration;
- hazard evaluation;
- evacuation decision support;
- route-safety evaluation;
- safe-zone evaluation;
- event-driven reassessment.

This repository exposes their **interfaces and responsibilities**, not their internal formulas or calibrated implementation.

## Data layer

Planned data categories include:
- wildfire / thermal detections;
- citizen observations;
- professional observations;
- weather;
- terrain;
- vegetation / fuel layers;
- road networks;
- safe-zone records;
- geospatial administrative data.

Production source selection and licensing will be documented separately.

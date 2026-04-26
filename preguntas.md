# SmartLog Azucarera - Project 3 Questions (Phase 2)

Context: a (fictitious) sugar factory wants to start with a small, low-cost monitoring system that can later scale to dashboards and IT integrations. SmartLog Azucarera is a local-first logger that simulates sensor readings, stores them in SQLite, and produces daily JSON backups.

## 6a) Strategic objectives

What specific strategic objectives of the company does your software address?

- Reduce unplanned downtime by detecting overheating conditions early (warning) and forcing a safe stop (critical threshold).
- Improve traceability and auditability by keeping a structured historical log of process variables (temperature/humidity).
- Enable incremental digitalization: start with a single workstation, then extend toward dashboards and integrations.

How does the software align with the overall digitalization strategy?

- It establishes a minimal data pipeline (capture -> validate -> store -> backup -> visualize) that can later be connected to SCADA/MES/ERP or a cloud platform.
- It standardizes a data model (timestamp, measurements, status) to avoid ad-hoc spreadsheets and manual logging.

## 6b) Business/production and communications areas

Which areas of the company benefit the most (production, business, communications)?

- Production/operations: real-time awareness of process conditions and alarms; supports safer operating procedures.
- Quality and business reporting: consistent logs enable basic KPI tracking and later analytics.
- Communications/maintenance: shared, readable artifacts (DB + JSON backups + dashboard) reduce friction between IT/OT and make incident discussion easier.

What operational impact do you expect on daily operations?

- Less manual paperwork and fewer unknown incidents due to missing logs.
- Faster troubleshooting (last readings, trends, and timestamps).
- Clear operator guidance for critical events (stop + manual reset procedure).

## 6c) Areas susceptible to digitalization

Which areas are most susceptible to being digitalized with your software?

- Equipment monitoring for critical assets (boilers, dryers, conveyors, evaporation units) where temperature is a key variable.
- Shift handover reporting (what happened, when, and under what readings).
- Basic maintenance planning driven by recorded trends (threshold crossings, frequent warnings).

How will digitalization improve operations in those areas?

- Improves continuity of information across shifts and teams.
- Enables simple trend analysis to identify recurring issues.
- Provides a foundation for automated alerts and future integrations.

## 6d) Fit between digitalized and non-digitalized areas

How do digitalized areas interact with non-digitalized ones?

- Operators still perform physical inspections and manual interventions; SmartLog adds a reliable record of what the sensors said at decision time.
- When some equipment is not instrumented, SmartLog outputs can be combined with manual checklists (non-digital inputs) during audits or investigations.

What improvements would you propose to integrate these areas?

- Add a small operator note field (optional) for manual annotations tied to a timestamp.
- Define a simple export interface (JSON/CSV) so office IT tools can consume the data without direct DB access.
- Introduce an asset registry (machine id, location) to link digital logs to non-digital maintenance documents.

## 6e) Present and future needs

What current needs does the software solve?

- A consistent log of key variables without requiring internet connectivity.
- A repeatable backup mechanism (daily JSON) for basic resilience.
- Operator-facing alerts tied to clear thresholds.

What future needs could be addressed by extensions?

- Real sensor ingestion (Modbus/OPC-UA) instead of simulation.
- Integrity controls for backups (signing/HMAC) and access controls for the DB.
- Data retention policies and automated archiving.
- Integration with a dashboard platform and/or a cloud data lake.

## 6f) Relation to enabling technologies (THD)

Which enabling technologies are used and how do they impact company areas?

- IoT/edge concept (simulated sensors): models how OT signals become IT data.
- Local data storage (SQLite): low-cost, low-maintenance persistence on the edge.
- Cloud-like backups (daily JSON in a dedicated folder): demonstrates the backup/export pattern that can later map to object storage.
- Lightweight web visualization (Streamlit demo): improves accessibility for non-developers.

What specific benefits does implementing these technologies provide?

- Faster decision-making from accessible historical data.
- Better alignment between OT operations and IT reporting needs.
- Lower barrier to adoption (works offline, minimal infrastructure).

## 6g) Security gaps

What potential security gaps could arise when implementing this software?

- Local database and backups may be readable/alterable by unauthorized users if the workstation is not hardened.
- Lack of backup integrity verification (JSON can be edited).
- If moved to a network share or cloud, credentials and access policies become critical.

What concrete measures would you propose to mitigate them?

- Enforce OS-level hardening: least privilege, disk encryption, restricted access to `data/` and `cloud_backup/`.
- Add integrity mechanisms for backups (e.g., signed backups with an HMAC key stored securely).
- Introduce basic auditing (who started/stopped the logger) if used in regulated environments.
- If networked, use TLS and scoped credentials, and avoid exposing SQLite directly.

## 6h) Data handling and analysis

How is data managed and what methodologies are used?

- Capture: generate a reading (or later, ingest from sensors).
- Validate: discard invalid humidity values (outside 0..100).
- Store: insert into a normalized SQLite table for structured querying.
- Backup: append into a daily JSON file for portability and resilience.
- Analyze: trends can be visualized in the demo dashboard and exported for further tooling.

How do you ensure data quality and consistency?

- Explicit schema with required fields and types (SQLite table).
- Simple validation rules at ingestion time.
- Time is recorded in UTC for consistent cross-system correlation.
- Backups are written in a consistent daily format.

## 6i) Integration between data, applications, and platforms

How do systems and data interact? Provide examples.

- The logger writes to SQLite and JSON backups; the Streamlit demo reads SQLite to visualize trends.
- JSON backups can be moved to another platform (shared drive or object storage) without changing the logger.

Proposals to improve interoperability.

- Add an export command to produce CSV/JSON bundles for BI tools.
- Define a stable schema/version for the exported format.
- Replace the `cloud_backup` folder with an object storage adapter while keeping the same interface.

## 6j) Changes documented according to strategy

How are changes recorded and linked to strategic objectives?

- `DEVLOG.md` explains changes in terms of project goals: open-source readiness, accessibility, and future extensibility.

Devlog usage.

- Each milestone should add an entry describing the change, why it exists, and which strategic objective it supports (traceability, safety, integration, etc.).

## 6k) Human resources suitability

What skills are needed to develop and maintain this software?

- Python fundamentals, packaging conventions, and code review practices.
- Basic database knowledge (SQLite, schema evolution, query patterns).
- OT/IT awareness (sensor data, timestamps, operational constraints).
- Security basics (least privilege, integrity, secure key storage if signing is added).

What training strategies would you propose for future contributors?

- Provide good first issue tasks in the tracker (docs improvements, small refactors).
- Keep a short onboarding section in `CONTRIBUTING.md` with reproducible commands.
- Add small, focused examples (how to add a sensor field, how to add an export format).


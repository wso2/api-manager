# Federated Gateway — Overview

## What is a Federated Gateway?
A **Federated Gateway** is an architectural pattern that allows multiple API gateway instances (often deployed in different data centers or cloud regions) to operate in a coordinated manner. Federation enables scaling, locality of traffic, and multi-tenant scenarios while preserving a central control plane for API management.

## Key concepts
- **Control plane vs Data plane** — The control plane manages API lifecycle, policies, and configuration; the data plane (gateways) handles runtime traffic enforcement.
- **Gateway federation** — Multiple gateway instances share configuration and policies from a central management plane.
- **Tenant and domain isolation** — Gateways can serve different tenant domains with isolated routing and policies.

## Typical use cases
- Multi-region or multi-DC deployments for low latency.
- Regulatory or data residency requirements that require traffic to stay within geographical boundaries.
- High availability and failover configurations.

## Deployment considerations
- **Configuration synchronization:** Use a reliable sync mechanism (push from control plane or pull by gateways).
- **Policy compatibility:** Ensure gateways support the same policy set and runtime features.
- **Monitoring and logging:** Centralize telemetry from all gateways for unified observability.

## Related topics
- API Manager control plane and gateway deployment
- Gateway clusters and scaling
- Security and tenant isolation

For more detailed examples and configuration steps, see the Gateway deployment section in this documentation.

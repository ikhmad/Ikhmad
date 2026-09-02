import { createIncident, createSOS, IncidentStatus } from "./models.js";

const incident = createIncident({
  id: "IKH-DEMO-001",
  latitude: 36.7538,
  longitude: 3.0588,
  observationType: "SMOKE_OR_FIRE"
});

console.log("Citizen report submitted:");
console.log(incident);

incident.status = IncidentStatus.UNDER_REVIEW;
console.log("\nCommand center receives incident:");
console.log(incident);

incident.status = IncidentStatus.CONFIRMED;
console.log("\nOperator updates incident status:");
console.log(incident);

const sos = createSOS({
  id: "SOS-DEMO-001",
  latitude: 36.7541,
  longitude: 3.0602,
  incidentId: incident.id
});

console.log("\nCitizen SOS received by command center:");
console.log(sos);

console.log(
  "\nNOTE: Confidence, hazard prediction, route scoring and safe-zone scoring " +
  "are intentionally not implemented in this public demo."
);

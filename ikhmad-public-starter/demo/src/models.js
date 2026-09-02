export const IncidentStatus = Object.freeze({
  REPORTED: "REPORTED",
  UNDER_REVIEW: "UNDER_REVIEW",
  PROBABLE: "PROBABLE",
  CONFIRMED: "CONFIRMED",
  ACTIVE: "ACTIVE",
  CONTROLLED: "CONTROLLED",
  CLOSED: "CLOSED",
  REJECTED: "REJECTED"
});

export function createIncident({ id, latitude, longitude, observationType }) {
  return {
    id,
    status: IncidentStatus.REPORTED,
    observationType,
    location: { latitude, longitude },
    createdAt: new Date().toISOString()
  };
}

export function createSOS({ id, latitude, longitude, incidentId = null }) {
  return {
    id,
    status: "RECEIVED",
    incidentId,
    location: { latitude, longitude },
    createdAt: new Date().toISOString()
  };
}

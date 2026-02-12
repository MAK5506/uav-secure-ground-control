# 🏗 System Architecture

## High Level Architecture Diagram

[ UAV / Flight Controller ]
|
| AES-256 Encrypted Telemetry
| (MQTT / TCP)
|
[ Secure Gateway ]
|
| WebSocket / REST API
|
[ Backend Server (FastAPI) ]
|
| PostgreSQL / Redis
|
[ Web Ground Control Station ]


---

## System Components

### 1. UAV / Flight Controller
Responsible for:
- Sensor data acquisition
- Telemetry packet generation
- AES-256 encryption
- Secure data transmission

### 2. Secure Gateway
Responsible for:
- Encrypted packet validation
- Message routing
- Protocol translation

### 3. Backend Server (FastAPI)
Responsible for:
- WebSocket telemetry streaming
- REST API services
- Data storage
- Authentication & authorization

### 4. Web Ground Control Station
Responsible for:
- Real-time monitoring dashboard
- Command transmission
- Data visualization
- System logging

---

## Security Architecture

- AES-256 encrypted telemetry channel
- Token-based authentication
- Secure WebSocket (WSS)
- Optional TLS mutual authentication

---

## Scalability Design

- Microservice-ready architecture
- Docker-based deployment
- Horizontal scalability supported

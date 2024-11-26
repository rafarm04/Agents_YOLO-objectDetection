# Agents_YOLO-objectDetection

# Coordinated Patrolling Simulation

This project showcases a **multi-agent system** designed to address urban security challenges by simulating coordinated patrolling in open-risk areas. The system integrates advanced artificial intelligence techniques, object detection, and inter-agent communication to detect and respond to potential security threats.

## Agents in the Simulation

### 1. **DroneAgent**  
   - **Primary Role**: Patrols the environment by flying over the designated area and searching for suspicious activity.  
   - **Object Detection**: Utilizes **YOLO (You Only Look Once)** to detect anomalies or suspicious objects.  
   - **Actions**:  
     - If suspicious activity is detected, it alerts the **SecurityAgent**.  
     - Waits for further instructions from the **SecurityAgent** to confirm or resolve the alert.  

### 2. **CameraAgent**  
   - **Primary Role**: Monitors specific locations using stationary surveillance.  
   - **Object Detection**: Employs **YOLO** to identify potential threats or suspicious behaviors.  
   - **Actions**:  
     - If suspicious activity is detected, it alerts the **DroneAgent**.  
     - Requests the **DroneAgent** to verify the threat by inspecting the location.  

### 3. **SecurityAgent**  
   - **Primary Role**: Central authority for threat verification and decision-making.  
   - **Actions**:  
     - Responds to alerts from the **DroneAgent** or **CameraAgent**.  
     - Takes control of the **DroneAgent** to further investigate suspicious activity.  
     - Decides whether to escalate by sending a security alert or dismiss the case as a false alarm.  

## Technologies Used

### Environment Design and Simulation  
- **Unity**: Created the simulation environment, incorporating agent behaviors, navigation, and visual feedback for testing the system.  

### Object Detection  
- **YOLO**: Integrated object detection model for identifying suspicious activity in real-time, providing agents with situational awareness.  

### Communication Between Systems  
- **Flask**: Developed a Python server to handle object detection and inter-agent communication logic.  
- **UnityWebRequest**: Facilitated seamless communication between Unity and the Flask server, ensuring agents and the object detection model work in sync.  

## How It Works  
1. **Surveillance and Detection**:  
   - The **DroneAgent** patrols the area, while the **CameraAgent** monitors fixed points. Both use YOLO for object detection.  

2. **Alert System**:  
   - If the **CameraAgent** detects suspicious activity, it alerts the **DroneAgent**, which inspects the location for verification.  
   - If the **DroneAgent** detects suspicious activity, it directly alerts the **SecurityAgent**.  

3. **Verification and Decision**:  
   - The **SecurityAgent** takes control of the **DroneAgent** to investigate and confirm the threat.  
   - Based on the findings, the **SecurityAgent** either sends a security alert or dismisses the case.  

## Key Features  
- Real-time coordination between agents for efficient patrolling.  
- Robust integration of AI-driven object detection (YOLO) into a Unity simulation.  
- Scalable communication framework using Flask and UnityWebRequest.  
- A realistic testing environment for simulating urban security scenarios.  

This project demonstrates how multi-agent systems and AI can work together to enhance urban safety by detecting and mitigating potential threats effectively.

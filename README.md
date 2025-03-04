# Headout-Globetrotter-Challenge
Globetrotter is a full-stack web app where users get cryptic clues about a famous place and must guess which destination it refers to. Once they guess, they’ll unlock fun facts, trivia, and surprises about the destination!

![og-image](https://github.com/user-attachments/assets/15188907-3c13-4c0a-b1c7-d7500ccdf388)

## 🚀 Live Demo
[To Play Globetrotter, Click Here](https://extraordinary-creation-production.up.railway.app/)

## 🛠 Tech Stack & Architecture

### Backend
- **Framework**: FastAPI
- **Database**: MongoDB
- **Key Features**:
  * RESTful API design
  * Async support
  * Data validation
  * Efficient database operations

### Frontend
- **Framework**: Vue.js
- **Styling**: Tailwind CSS
- **Technologies**:
  * HTML5
  * Responsive design
  * Component-based architecture

### Deployment
- **Platform**: Railway
- **Continuous Deployment**: Automated CI/CD pipeline

## 🎯 Project Overview

### 1. Dataset & AI Integration
- [ ] Create a comprehensive dataset of 100+ destinations
- [ ] Utilize AI tools for dataset expansion
- [ ] Dataset must include:
  * Cryptic clues for each destination
  * Fun facts
  * Interesting trivia

### 2. Web Application Features
#### Gameplay Mechanics
- [ ] Randomly select 1-2 clues for a destination
- [ ] Multiple-choice destination guessing
- [ ] Immediate feedback system
  * Correct Answer:
    - Confetti animation
    - Reveal a fun fact
  * Incorrect Answer:
    - Sad-face animation
    - Reveal a fun fact
- [ ] 'Play Again' or 'Next' button to load a different destination
- [ ] User score tracking
  * Total correct answers
  * Total incorrect answers

#### Backend Requirements
- [ ] Store dataset on backend
- [ ] Prevent users from accessing all questions/answers through source code

### 3. "Challenge a Friend" Feature
#### User Registration
- [ ] Username entry before playing
- [ ] Create user profile in the system

#### Friend Challenge Mechanism
- [ ] 'Challenge a Friend' button functionality
- [ ] Share popup with:
  * Dynamic invite image
  * WhatsApp invitation link
- [ ] Display invitee's score to the invited friend
- [ ] Invitation link provides full game access

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/BelieveInTheLimitless/Headout-Globetrotter-Challenge.git
cd Headout-Globetrotter-Challenge
```

### 2. MongoDB Database Configuration
```bash
# Make sure Docker is already present in your system
docker run -d -p 27017:27017 --name mongodb mongo:latest
```

### 3.Building and running the backend
```bash
# Inside main repository
cd backend
# Setup python virtual environmnent
python3 -m venv .venv
# Activate virtual envirornment
source .venv/bin/activate
# Install dependencies
pip3 install -r requirements.txt
#Run the uvicorn server
uvicorn app.main:app --reload
#open the server on localhost:8080
#To exit the application, ctrl+c, then
deactivate
```

### 4. Building and running the frontend
```bash
#Inside main repository
cd frontend
# Install packages
npm install
# Run and open the frontend
npm run dev
#To exit the application, ctrl+c
```

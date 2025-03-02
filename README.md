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

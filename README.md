# Choice Based Game

An interactive, choice-driven storytelling application built with [Streamlit](https://streamlit.io/). Users participate in a dynamic narrative, making decisions that influence the direction and outcome of the story. The interface features a modern, dark-themed chat layout with avatars and a sidebar for instructions and story review.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Features

- **Dark Mode Interface:** All chat cards, avatars, and sidebars use a cohesive dark color scheme for comfortable reading.
- **Choice-Based Gameplay:** The story unfolds based on user input. Users can type their own prompts or select from provided choices.
- **Persistent Session State:** The app remembers the conversation and story progress during the session.
- **Sidebar Guidance:** Helpful instructions and an expandable full-story view are always accessible.
- **Customizable Agents and Tasks:** Easily modify the story logic and agent behavior by editing the agent and task modules.

---


## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone or Download the Repository**

   ```
   git clone <repository-url>
   cd "Choice Games"
   ```

2. **Install Required Packages**

   ```
   pip install streamlit crewai
   ```

   > _You may need to install additional dependencies for your custom agents or tasks._

---

## Project Structure

```
Choice Games/
├── app.py
├── Agents/
│   └── Story_agent.py
└── Task/
    └── Story_task.py
```

- **app.py:** Main Streamlit application file.
- **Agents/Story_agent.py:** Defines the story agent logic.
- **Task/Story_task.py:** Contains the story task logic.

---

## Usage

1. **Start the Application**

   ```
   streamlit run app.py
   ```

2. **Interact with the Game**

   - Enter a story prompt in the chat input to begin your adventure.
   - The assistant will respond with a story segment and present choices.
   - Copy and paste one of the choices into the chat input to continue.
   - The sidebar provides game information and an expandable view of the full story so far.

3. **Session State**

   - Your choices and the story are preserved during your session.
   - Refreshing the page will reset the session.

---

## Customization

- **Change Story Logic:**  
  Edit `Agents/Story_agent.py` and `Task/Story_task.py` to modify how the story is generated or how choices are handled.

- **Modify Interface:**  
  Adjust the CSS section in `app.py` to change colors, fonts, or layout.

- **Add Features:**  
  You can extend the app with new features such as saving stories, user authentication, or multimedia support.

---

## Troubleshooting

- **Module Not Found:**  
  Ensure your folder structure matches the import paths in `app.py`.

- **Streamlit Not Launching:**  
  Make sure Streamlit is installed and you are running the command in the correct directory.

- **Agent/Task Errors:**  
  Check your custom agent and task code for syntax or logic errors.

---

## License

This project is for personal or educational use only.  
Do not redistribute or use for commercial purposes without permission.

---

_Made with [Streamlit](https://streamlit.io/) and ❤️_

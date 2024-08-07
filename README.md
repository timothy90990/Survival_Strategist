# Survival_Strategist
COM-430: Software Engineering Group Project

![image](https://github.com/user-attachments/assets/da205c91-2cec-4b05-9af3-4821af23f3d1)



## Overview
"Castaway Retreat: Mind and Survival" integrates survival strategy with inspiring content on mental health and awareness. This project aims to design, develop, and release a software application that is immersive, provides mental health education, and works on multiple platforms.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Files](#project-files)

## Project Structure
Structure of the project is still being worked on. Tenative structure is as follows:
```
castaway_retreat/
├── src/
│   ├── media/
│   │   ├── character.png
│   ├── modules/
│   │   ├── user_interface.py
│   │   ├── quotes.py
│   │   └── game_logic.py
│   ├── config.py
│   ├── quotes.json
├── tests/
│   ├── test_user_interface.py
│   └── test_game_logic.py
├── .gitignore
├── CHANGELOG.md
├── README.md
├── requirements.txt
└── main.py
```

### Installation
1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
2. Open a terminal or Command Prompt.
3. Clone the repository from GitHub by running the following command:
    ```bash
    git clone https://github.com/thechristopherbartlett/Survival_Strategist.git
    ```
4. Navigate to the project directory:
    ```bash
    cd Survival_Strategist
    ```
5. Install the required dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
To run the application, execute the following command in your terminal or Command Prompt:
```bash
python main.py
```

## Project Files

### Root Directory
- **README.md**: This file, which provides an overview of the project and explains the structure of the files.
- **requirements.txt**: Lists all the dependencies required to run the project.
- **main.py**: The entry point of the application. It initializes and runs the main program.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **CHANGELOG.md**: Contains the log of changes made to the project.

### Source Code Directory: `src`
- **config.py**: Contains configuration settings for the application.

### Modules Directory: `src/modules`
- **user_interface.py**: Handles the user interface components and interactions.
- **quote_generator.py**: Manages the quote generation feature, providing inspirational and mental health-related quotes.
- **mental_health_education.py**: Contains educational content and resources related to mental health.
- **survival_strategy.py**: Implements features and content related to survival strategies.
- **database.py**: Manages database interactions, including creating and querying the database.

### Tests Directory: `tests`
- **test_user_interface.py**: Contains unit tests for the user interface module.
- **test_quote_generator.py**: Contains unit tests for the quote generator module.
- **test_mental_health_education.py**: Contains unit tests for the mental health education module.
- **test_survival_strategy.py**: Contains unit tests for the survival strategy module.
- **test_database.py**: Contains unit tests for the database module.

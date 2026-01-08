# python-accessible-game

## Overview
This project is a Python-based game designed with accessibility in mind, allowing users to play using controllers and providing support for screen readers. The game features a rich graphical interface and engaging gameplay while ensuring that it is accessible to players with disabilities.

## Features
- **Accessibility Support**: The game includes features for screen reader support and controller accessibility, making it playable for a wider audience.
- **Controller Input**: Full support for various controllers, allowing for a seamless gaming experience.
- **Audio Descriptions**: Visually impaired players can receive audio descriptions of game elements through integrated screen reader functionality.
- **Localization**: The game supports multiple languages, starting with English (US).

## Project Structure
```
python-accessible-game
├── src
│   ├── main.py          # Entry point of the game
│   ├── game.py          # Game logic and state management
│   ├── ui.py            # User interface management
│   ├── input.py         # Input handling for keyboard and controllers
│   ├── controllers.py    # Controller input management and accessibility features
│   ├── audio.py         # Audio playback management
│   ├── accessibility
│   │   ├── __init__.py  # Accessibility module initialization
│   │   ├── screen_reader.py # Screen reader functionality
│   │   └── controller_labels.py # Controller button mappings
│   └── resources
│       └── locale
│           └── en-US.json # Localization strings
├── tests
│   ├── test_game.py     # Unit tests for game logic
│   └── test_input.py    # Unit tests for input handling
├── requirements.txt      # Project dependencies
├── pyproject.toml       # Project configuration
└── README.md            # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd python-accessible-game
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the game, execute the following command:
```
python src/main.py
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
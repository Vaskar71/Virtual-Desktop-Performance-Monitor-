# Virtual Desktop Performance Monitor

<img width="362" alt="Image" src="https://github.com/user-attachments/assets/1e315cab-bd9e-4808-93ef-98083ef70fc0" />

> A real-time system performance monitoring desktop application built in Python.

## Description
Virtual Desktop Performance Monitor is a Python desktop application that continuously monitors your system's CPU, memory, and network usage. It displays performance metrics in a user-friendly Tkinter GUI and logs data to a CSV file for further analysis. 

## Table of Contents
- [Installation/Getting Started](#installationgetting-started)
- [Usage](#usage)
- [Features](#features)
- [Configuration/Customization](#configurationcustomization)
- [Contributing](#contributing)
- [License](#license)
- [Contact/Support](#contactsupport)
- [Credits/Acknowledgments](#creditsacknowledgments)
- [Screenshots](#screenshots)

## Installation/Getting Started
1. **Prerequisites:**
   - Python 3.x installed ([Download Python](https://www.python.org/downloads/)).
   - Install the required package `psutil`:
     ```bash
     pip install psutil
     ```
2. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/VirtualDesktopPerformanceMonitor.git
   cd VirtualDesktopPerformanceMonitor
   ```
3. **Run the Application:**
   - Open your terminal or command prompt in the project directory.
   - Execute the application:
     ```bash
     python main.py
     ```

## Usage
When you run the application, a window will appear displaying real-time performance metrics:
- **CPU Usage**
- **Memory Usage**
- **Network Usage (Bytes Sent/Received)**
- A log panel shows each update and all data is saved to `performance_log.csv`.

Feel free to modify the code to add more metrics or adjust the user interface.

## Features
- **Real-time Monitoring:** Continuously updates system performance metrics.
- **User-friendly GUI:** Built using Python's Tkinter module.
- **CSV Logging:** Automatically logs data for performance analysis.
- **Beginner Friendly:** Well-commented code and clear structure.
- **Extensible:** Easily add new metrics or customize the display.

## Configuration/Customization
- **CSV File Name:** Adjust the CSV filename in the `CSVLogger` class in `main.py`.
- **Refresh Interval:** Modify the update interval in the `update_metrics` method (currently set to 1 second).
- **UI Customization:** Customize widget styles and layout in the `create_widgets` method.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (e.g., `git checkout -b feature/your-feature`).
3. Commit your changes with clear comments.
4. Push the branch and open a Pull Request.
Please follow the existing code style and add documentation as needed.

## Credits/Acknowledgments
- [psutil](https://github.com/giampaolo/psutil) for providing robust system monitoring capabilities.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the built-in GUI framework.
- Inspiration from various beginner-friendly real-time monitoring projects.



# YouTube Video Manager

A simple Python-based command-line application for managing a database of YouTube videos. This project demonstrates basic database operations (CRUD - Create, Read, Update, Delete) using SQLite and a clean user interface for interaction.

## Features
- **List Videos**: View all the videos stored in the database in a tabular format.
- **Add Videos**: Insert new videos with their name and duration.
- **Update Videos**: Modify the name or duration of an existing video.
- **Delete Videos**: Remove a video by its unique ID.
- **User-Friendly Interface**: Interactive menus for seamless navigation.

## Requirements
- Python 3.7 or higher
- SQLite (comes pre-installed with Python)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yt_manager.git
   cd yt_manager
   ```
2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```
   *(No additional dependencies are required for this project unless you plan to extend it.)*

3. Run the application:
   ```bash
   python yt_manager.py
   ```

## Usage
1. When you start the application, you will see the main menu with the following options:
   ```
   ========== YouTube Manager ==========
   1. List Videos
   2. Add Videos
   3. Update Videos
   4. Delete Videos
   5. Exit
   =====================================
   ```

2. **List Videos**:
   - Select `1` to view a tabular list of all videos stored in the database.

3. **Add Videos**:
   - Select `2` and enter the video name and duration (e.g., `00:03:15` for 3 minutes and 15 seconds).

4. **Update Videos**:
   - Select `3`, enter the ID of the video to update, and provide the new name and duration.

5. **Delete Videos**:
   - Select `4`, and enter the ID of the video you want to delete.

6. **Exit**:
   - Select `5` to quit the application.

## Project Structure
```
.
├── videos.db              # SQLite database file
├── yt_manager.py          # Main Python script
├── README.md              # Project documentation (this file)

```

## Example Output
### Listing Videos:
```
==================== Video List ====================
ID    Name                          Duration  
--------------------------------------------------
1     Python Tutorial               01:30:45  
2     Django Basics                 02:15:30  
3     React Guide                   01:50:00  
==================================================
```
### Adding a Video:
```
Enter the video name: Flask Introduction
Enter the video duration (e.g., HH:MM:SS): 00:45:00
[INFO] Video added successfully.
```

## License
This project is licensed under the MIT License. Feel free to use and modify it for your needs.

## Contributions
Contributions are welcome! If you have suggestions or improvements, feel free to open a pull request or submit an issue on GitHub.

## Author
**Roshan Kumar Singh**

This project was created as part of my Python learning journey, inspired by a tutorial from the *Chai aur Code* YouTube channel. Connect with me on [GitHub](https://github.com/Roshansingh9) or reach out for collaboration!


# Smart File Organizer (Python Command-Line Utility)

## Problem Statement
On my system, folders such as **Downloads** and **Desktop** become cluttered with different file types like documents, images, videos, and installers. This makes it difficult to quickly locate files and requires manual, repetitive organization.

## Solution
This project is a **Python-based command-line utility** that automatically organizes files in a given directory into categorized folders based on their file extensions.  
The solution uses **only Python standard libraries** and focuses on clean logic, error handling, and usability.

## Features
- Organizes files by type (Documents, Images, Videos, Archives, Others)
- Accepts directory path as a command-line argument
- Automatically creates folders if they do not exist
- Handles invalid paths and empty directories safely
- Lightweight and easy to run

## Folder Classification
| Category   | Extensions |
|-----------|------------|
| Images    | jpg, jpeg, png |
| Documents | pdf, txt, docx |
| Videos    | mp4, mkv |
| Archives  | zip, rar |
| Others    | All remaining file types |

## How to Run

### 1. Prerequisites
- Python 3.x installed
- Python added to system PATH
- python file_organizer.py "C:\Users\LENOVO\Downloads"
## sample Output
Moved: resume.pdf -> Documents
Moved: photo.jpg -> Images
Moved: video.mp4 -> Videos
Moved: setup.exe -> Others
File organization completed successfully.

Verify installation:
```bash
python --version

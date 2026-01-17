# File_organizer
Smart File Organizer (Java CLI Utility)
Problem
My Downloads folder gets cluttered with mixed file types, making it hard to locate files.

Solution
This Java command-line utility automatically organizes files into folders based on their extensions.

How to Run
Compile the program: javac FileOrganizer.java

Run the program: java FileOrganizer "C:\Users\YourName\Downloads"

Design Decisions
Used Java Standard Library only
HashMap for easy file-type mapping
Command-line arguments for flexibility
Safe error handling for invalid paths and permissions
Assumptions
Files with unknown extensions go into "Others"
Folder structure is created automatically

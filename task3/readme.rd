# 📂 Task Automation with Python
Move `.jpg` Files Using Python

## 🎯 Objective
The objective of this project is to automate the task of moving all .jpg files from one folder to another using Python.

## 🧠 Description
This project is a simple automation script that scans a source folder, identifies all .jpgfiles, and moves them to a destination folder.
It helps in reducing manual effort when handling multiple image files.


## ⚙️ How It Works
1. The script reads all files from the source folder.
2. It checks each file to see if it ends with jpg.
3. If the condition is true, the file is moved to the destination folder.
4. If the destination folder does not exist, it is created automatically.
5. The process continues until all .jpg files are moved.


## 🛠 Technologies Used
* Python
*os module
* shutil module

## ✨ Features
* Automatically moves all .jpgfiles
* Creates destination folder if not present
* Simple and easy to use
* Saves time and effort


## ▶️ How to Run
1. Create two folders:
   *source (contains `.jpg` files)
   * destination (empty folder)

2. Update folder paths in the script:
   source_folder = "source"
   destination_folder = "destination"
3. Run the Python script:
   python your_file_name.py
   

## 📥 Input
* A folder containing `.jpg` files
## 📤 Output
* All `.jpg` files moved to the destination folder


## ⚠️ Limitations
* Works only for `.jpg` files
* Does not handle duplicate file names
* No graphical interface


## ✅ Conclusion
This project demonstrates how Python can be used to automate simple and repetitive tasks efficiently. It is useful for beginners to understand file handling and automation concepts.


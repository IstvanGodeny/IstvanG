# 📝 Portfolio Website

A Flask-based portfolio website showcasing my development projects with a clean design and interactive features.  
It highlights applications such as **Note Application**, **Tic Tac Toe Game**, and **Image Watermarking Tool** with dedicated pages, screenshots, and descriptions.

---
## ✨ Features

- Built with **Flask** and **Jinja2 templating**
- Showcases multiple Python projects with screenshots and descriptions
- Responsive design using **Bootstrap** and custom CSS
- Interactive **Lottie animations** and SVG icons
- Organized structure with `templates/` and `static/` folders
- Ready for deployment with **Procfile** and `requirements.txt`
- Optimized for presenting projects professionally online

---
## 🛠️ Technologies Used

- **Python 3.10+**
- **Flask**
- **Jinja2**  
- **Bootstrap / CSS3**
- **Lottie animations**  
- **HTML5**
- **Minimal JavaScript**

---
## 📂 Project Structure

├── main.py                    # Application entry point

├── static [folder]             # Main window with note list

├──────── static [folder]             # Main window with note list

├── note_card.py               # Custom note card widget

├── add_new_note_card.py       # Dialog for adding notes

├── edit_note_card.py          # Dialog for editing notes

├── notes.sqlite               # SQLite database (auto-generated)

└── requirements.txt           # List of the dependencies

---
## 🖥️ Cross-Platform Support

This app runs on:

- Windows
- macOS
- Linux

> ✅ No installation required — only Python 3.8+ and a few standard packages.

---
## 🎓 Author Note

This is a demo project, created as part of my learning journey as a junior Python developer.
I focused on building a functional, maintainable, and visually clean app, without unnecessary complexity.

---
## 📝 Licence

MIT License – feel free to use, modify, and learn from it!

---
## 🚀 How to Run

1. Download files and store them in a folder.

2. (Optional) Create a virtual environment in the folder where the files were downloaded.
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the application
```bash
python main.py
```

# DOCK  

## About the Project 
**DOCK** is a digital diary where you can record your days, thoughts and memories.
The unique feature is **time control**: you decide **when (or if) want to make public**.

It could be in 2 years... or in 20. The choice is yours. 
Each diary works like a small **"message in a bottle"**, launched into time - ready to be found and read in the future

## Technologies Used 
This project was built with:  

- **Python (Django Framework)**  
- **JavaScript**  
- **HTML5**  
- **Tailwind CSS**  
- **Alpine.js**  

---

## How to Use

Notes
Make sure you have **Python 3.x** and **Node.js** installed on your machine.

### 1. Clone this repository 
```
git clone https://github.com/JonasFranc1sco/DOCK.git
cd DOCK/
```
### 2. Install Node dependences
```
npm install
```
### 3. Run database migrations
```
python manage.py makemigrations accounts
python manage.py makemigrations page
python manage.py migrate
```
By default, ,the project uses SQLite3.
If you prefer, you can change the database in the settings.py file, located in the main diary/ directory.

### 4. Start server locally
In two separate terminals, run:
```
python manage.py tailwind start
python manage.py runserver
```
The project will be available at:
http://localhost:8000

Adjust the .env file as needed (if you want to use environment variables).

Roadmap
features planned for future versions:

 Upload and edit user profile images

 Search system within diary entries

 User search system

 Light/Dark theme customization

Contribuitions
Contribuitions are always welcome!
Feel free to open issues and pull requests.

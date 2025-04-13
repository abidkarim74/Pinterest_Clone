Pinterest Clone
A Pinterest-like web application built using Django, Django REST Framework, React, and PostgreSQL. This project replicates core features of Pinterest such as creating pins, uploading images, user profiles, and browsing a dynamic feed. It includes secure authentication using JWT tokens, a responsive frontend, and a RESTful API backend.

Features
User Authentication: Secure login, registration, and session management using JWT (JSON Web Tokens).

Pin Creation: Users can create pins with images and descriptions.

Image Uploads: Users can upload images to be displayed as pins.

Dynamic Feed: A dynamic feed of pins from all users, similar to Pinterest's main page.

User Profiles: Each user has a personal profile displaying their created pins.

Responsive Design: Fully responsive frontend for an optimal user experience on both desktop and mobile devices.

Technologies Used
Backend:

Django and Django REST Framework for building the API.

PostgreSQL for database management and storage.

JWT Authentication for secure user authentication and session management.

Frontend:

React for building the user interface.

Axios for handling HTTP requests to the backend.

Getting Started
Prerequisites
Make sure you have the following installed on your local machine:

Node.js (for React)

Python 3.x (for Django)

PostgreSQL (for database)

pip (Python package manager)

npm (Node package manager)

Setting Up the Backend (Django)
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/pinterest-clone.git
cd pinterest-clone
Set up a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up the PostgreSQL database:

Create a PostgreSQL database and update the DATABASES configuration in settings.py with your database credentials.

Apply migrations to set up the database schema:

bash
Copy
Edit
python manage.py migrate
Create a superuser to access the Django admin:

bash
Copy
Edit
python manage.py createsuperuser
Start the Django development server:

bash
Copy
Edit
python manage.py runserver
Setting Up the Frontend (React)
Navigate to the frontend directory:

bash
Copy
Edit
cd frontend
Install the required dependencies:

bash
Copy
Edit
npm install
Run the React development server:

bash
Copy
Edit
npm start
Testing
You can test the backend API using tools like Postman or cURL by sending requests to http://localhost:8000/api/.

The frontend can be accessed at http://localhost:3000/.

Environment Variables
Create a .env file in the root directory of the project to store your environment variables.

Example .env:

env
Copy
Edit
DATABASE_URL=postgres://user:password@localhost:5432/pinterest_clone_db
SECRET_KEY=your_secret_key
DEBUG=True
Contributing
Feel free to fork the repository, make changes, and submit a pull request. Contributions are welcome!

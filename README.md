Here are the setup and run instructions for both the backend and frontend of your project, along with a crucial note on adding initial data:

✅ Backend Setup & Run Instructions
Navigate to the backend project directory:

bash
Copier le code
cd backend
Create and activate a virtual environment (optional but recommended):

bash
Copier le code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copier le code
pip install -r requirements.txt
Apply database migrations:

bash
Copier le code
python manage.py migrate
Start the development server:

bash
Copier le code
python manage.py runserver
Add movie data via the API:

🔴 Important: Before using the frontend, you must add movie data through the backend API endpoint:

bash
Copier le code
POST /movies/
You can use tools like Postman or cURL to make a POST request with the required movie data.

✅ Frontend Setup & Run Instructions
Navigate to the frontend project directory:

bash
Copier le code
cd frontend
Install dependencies:

bash
Copier le code
npm install
Run the development server:

bash
Copier le code
npm start
Access the frontend:
Open your browser and go to:

arduino
Copier le code
http://localhost:3000
⚠️ Note
Ensure that the backend server is running and accessible at the API base URL used by the frontend (e.g., http://localhost:8000).

No movies will appear on the frontend unless you first add them via POST /movies/.

Let me know if you need example data or cURL/Postman examples for the POST /movies/ request.

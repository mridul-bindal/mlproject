🌾 Crop Recommendation System
This is a full-stack machine learning project that recommends the most suitable crop to grow based on environmental conditions such as Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, and Rainfall. The machine learning model was trained on the Crop Recommendation Dataset from Kaggle and integrated with a Flask backend and React frontend.

📂 Dataset
Source: Kaggle - Crop Recommendation Dataset

Path: /kaggle/input/crop-recommendation-dataset/Crop_recommendation.csv

Features Used:
N - Nitrogen content in soil

P - Phosphorus content in soil

K - Potassium content in soil

temperature - Average temperature

humidity - Relative humidity in %

ph - pH value of the soil

rainfall - Rainfall in mm

🎯 Objective
To build a machine learning model that predicts the optimal crop to cultivate based on given input parameters. The model is served using a Flask backend, and the frontend interface is built using React.

⚙️ Tech Stack
Layer	Technology
Frontend	React.js (with React Forms)
Backend	Flask (Python)
Model	Scikit-learn
Data Handling	Pandas, NumPy
Communication	JSON over HTTP (CORS enabled)

🔍 Model Information
Algorithm Used: RandomForestClassifier

Accuracy Achieved: 99.31% (0.9931818181818182)

Model Exported with: pickle

🔌 Backend - Flask
Reads input from the frontend via JSON POST requests.

Loads the trained model using pickle.

Returns crop predictions in JSON format.

Endpoint:

POST /predict

Content-Type: application/json

{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 20.87,
  "humidity": 82.00,
  "ph": 6.5,
  "rainfall": 202.93
}
Response:

{
  "prediction": "rice"
}
🌐 Frontend - React
Simple form built using React that captures 7 inputs (N, P, K, temperature, humidity, pH, rainfall).

Sends data to the Flask backend using the fetch API.

Displays prediction result on the UI.


🧩 Connecting React and Flask
React runs on http://localhost:3000 while Flask runs on http://localhost:5000. To enable communication between these two, CORS (Cross-Origin Resource Sharing) is configured in Flask using:

from flask_cors import CORS
CORS(app)

This allows the frontend and backend to communicate despite running on different ports during development.

🚀 How to Run the Project
1. Clone the Repository

git clone https://github.com/your-username/crop-recommendation-app.git
cd crop-recommendation-app

2. Setup Backend

cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
The backend will start on http://localhost:5000.

3. Setup Frontend

cd frontend
npm install
npm start
The frontend will start on http://localhost:3000.

📸 Screenshots

<img width="1100" height="888" alt="image" src="https://github.com/user-attachments/assets/65ffb698-db0e-419e-8fc5-091e32abf36a" />


Form Input UI

Prediction Output Display

📁 Project Structure

Thia is how your folder structure should look like if you are using it with react and flask api.  

<img width="383" height="767" alt="image" src="https://github.com/user-attachments/assets/49f25278-3789-4a57-aabc-f6909f0b9139" />


✅ Features

High accuracy ML model (99.31%)

Intuitive React UI for input

Real-time crop predictions

Full-stack integration using Flask & React

🛠 Future Improvements
Add user authentication

Store prediction history in database

Deploy on cloud using Docker and Nginx

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📜 License
MIT License

🙋‍♂️ Author
Mridul Bindal
Feel free to connect with me or raise issues in the repo for improvements.

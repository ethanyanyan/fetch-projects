# fetch-projects

Projects done as part of a take-home assessment by Fetch. Had 48 hour window to complete projects.

**Front-end project** (frontend folder)
Description: used Dog API to build an application where users can view an image gallery of their favorite dog breeds.
Features: 
  1. Filter search bar to filter dog breeds
  2. Autoplay gallery to display 3 pictures per dog breeds selected
Commands to run quasar app locally:
  1. cd frontend
  2. npm install
  3. npm install vue3-apexcharts apexcharts
  4. quasar dev

**Back-end project** (backend_be folder)
Description: Built a REST API using Flask that will help keep track of points and point transactions, served on port 8000, and endpoints accept and return JSON when required.
Features:
  1. Integrated with Frontend Quasar Webapp to display requests when adding, deducting, or obtaining total. (Both Backend API and frontend has to run locally)
Dependencies needed: Flask Flask-Cors

**Machine-learning project** (backend_ml folder)
Description: This project involves predicting the monthly count of scanned receipts for the year 2022, utilizing data from the year 2021. The prediction model is trained using Mini-batch Stochastic Gradient Descent and is based on Linear Regression techniques.
Features:
  1. Made a Flask API to be able to be called from Frontend for receipts data.
  2. Integrated with Frontend Quasar Webapp to display the graph of predicted receipt counts in 2022.
Dependencies: pandas torch torch.nn matplotlib.pyplot Flask Flask-Cors


# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY frontend/package*.json ./

# Install the project dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY frontend/ .

# Build the Quasar Vue.js project
RUN npm run build

# Expose the port the app runs on
EXPOSE 8080

# Define the command to run the application
CMD ["npm", "run", "start"]

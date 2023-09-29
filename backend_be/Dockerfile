FROM ubuntu:23.10
# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    unzip \
    python3 \
    python3-pip

# Set the working directory
WORKDIR /app

# install dependencies
RUN pip install Flask Flask-Cors

# Copy your Flask application code into the container
COPY be.py /app/

# Expose the port that your Flask application will run on
EXPOSE 8000

# Start your Flask application
CMD ["python3", "be.py", "--ip=0.0.0.0", "--port=8000", "--allow-root"]

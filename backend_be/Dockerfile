FROM ubuntu:23.10

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    unzip \
    python3 \
    python3-pip \
    python3-venv  # Install python3-venv for virtual environment support

# Set the working directory
WORKDIR /app

# Create a virtual environment
RUN python3 -m venv venv

# Activate the virtual environment
SHELL ["/bin/bash", "-c"]
RUN source venv/bin/activate

# Install dependencies within the virtual environment
RUN pip install Flask Flask-Cors

# Copy your Flask application code into the container
COPY be.py /app/

# Expose the port that your Flask application will run on
EXPOSE 8000

# Start your Flask application within the virtual environment
CMD ["venv/bin/python3", "be.py", "--ip=0.0.0.0", "--port=8000", "--allow-root"]

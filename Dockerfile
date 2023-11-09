# Use an official Python runtime as a parent image
FROM python:3.10-alpine

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Set the working directory in the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install pipenv and project dependencies
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copy the rest of the application code to the container
COPY . /app/

# Expose the port on which the Flask application will run
EXPOSE 5000

# Command to run the Flask application
CMD ["pipenv", "run", "flask", "run"]

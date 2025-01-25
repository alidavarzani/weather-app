FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY ./app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY ./app /app

# Copy the templates folder
COPY ./templates /app/templates

# Set the command to run the app
CMD ["python", "app.py"]

FROM python:3.12-slim

WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt requirements.txt

#Install the required dependencies and set up the dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

# Copy all files
COPY . .

CMD ["python", "app.py"]
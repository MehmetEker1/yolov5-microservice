FROM python:3.12-slim

WORKDIR /app

# requirements.txt dosyasını kopyalayın
COPY requirements.txt requirements.txt

# Gerekli bağımlılıkları yükleyin ve bağımlılıkları kurun
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

# Tüm dosyaları kopyalayın
COPY . .

CMD ["python", "app.py"]
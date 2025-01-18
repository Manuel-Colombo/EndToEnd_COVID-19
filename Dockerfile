# Usa un'immagine di base con Python
FROM python:3.9-slim

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia i file necessari nel container
COPY . /app

# Installa le dipendenze del progetto
RUN pip install --no-cache-dir -r requirements.txt

# Esponi la porta che il Flask server utilizza (default 5000)
EXPOSE 5051

# Comando per eseguire l'app Flask
CMD ["python", "app.py"]

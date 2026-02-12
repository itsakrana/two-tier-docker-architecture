FROM python:3.10-slim    # Uses a lightweight Python image

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m appuser   # Create a non-root user 'appuser' for security
USER appuser             # Switch to 'appuser' so app runs with limited permissions

EXPOSE 5000

CMD ["python", "app.py"]

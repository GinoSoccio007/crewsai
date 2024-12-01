FROM python:3.12-slim

WORKDIR /app

# Install dependencies
RUN pip install fastapi uvicorn python-multipart crewai langchain-openai

# Copy your application file
COPY app.py .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]

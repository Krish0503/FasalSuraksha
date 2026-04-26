# Use the official Python 3.11 slim image
FROM python:3.11-slim

# Create a user to avoid running as root (Hugging Face Spaces requirement)
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY --chown=user requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY --chown=user . .

# Expose the default port for Hugging Face Spaces (7860)
EXPOSE 7860

# Run the model download script, then start Gunicorn
CMD ["sh", "-c", "python download_model.py && gunicorn -b 0.0.0.0:7860 --workers 1 --timeout 120 app:app"]

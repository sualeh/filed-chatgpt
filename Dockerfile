FROM python:3.12.1-slim

# Set the working directory to /filed_chatgpt
WORKDIR /opt/filed_chatgpt/

# Copy the current directory contents into the container at /filed_chatgpt
COPY \
    . /opt/filed_chatgpt/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "./filed_chatgpt/filed_chatgpt.py"]


# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10-slim

WORKDIR /streamlitgcp

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/kkaarel/streamlitgcpterraform.git .

RUN dir -s 

RUN pip3 install -r ./streamlitgcp/requirements.txt \
    pip install --upgrade pip

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "./streamlitgcp/app.py", "--server.port=8080", "--server.address=0.0.0.0"]

# Project IA Documents

## Description
This project uses artificial intelligence to process and analyze documents. It leverages libraries such as Flask, OpenAI, and Pandas to create a web application that allows text and data analysis.

## Project Structure
- `back-end-doc-ia/`: Contains the back-end code using Flask.
  - `main.py`: Main application file for the Flask back-end.
  - `requirements.txt`: List of dependencies for the back-end.
  - `Dockerfile`: Dockerfile for the back-end.
- `app-documents-ia/`: Contains the front-end code using Vue.js with Vite.
  - `src/`: Source files for the front-end.
  - `package.json`: List of dependencies and scripts for the front-end.
  - `Dockerfile`: Dockerfile for the front-end.
- `docker-compose.yml`: Docker Compose file to orchestrate the back-end and front-end services.
- `.env`: Environment variables file.

## Installation

### Back-end (Flask)

1. Clone the repository:
    ```bash
    git clone https://github.com/antonio-dev2710/project-ia-documents.git
    cd project-ia-documents/back-end-doc-ia
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a [.env](http://_vscodecontentref_/0) file in the [back-end-doc-ia](http://_vscodecontentref_/1) directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

5. Run the Flask server:
    ```bash
    python main.py
    ```

### Front-end (Vue.js with Vite)

1. Navigate to the front-end directory:
    ```bash
    cd ../app-documents-ia
    ```

2. Install the dependencies:
    ```bash
    npm install
    ```

3. Run the development server:
    ```bash
    npm run dev
    ```

4. Access the web application at `http://localhost:3000`.

## Docker Deployment

### Dockerfile for Back-end (Flask)

Create a `Dockerfile` in the [back-end-doc-ia](http://_vscodecontentref_/2) directory:

```Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


FROM node:23.3.0

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000
CMD ["npm", "run", "preview"]
version: '3.8'

services:
  backend:
    build:
      context: ./back-end-doc-ia
    container_name: backend
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}

  frontend:
    build:
      context: ./app-documents-ia
    container_name: frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend

Running with Docker Compose

Create a .env file in the root of the project and add your OpenAI API key: <vscode_annotation details='xxxxxxxxxxxxxxxxxxxxxx'> </vscode_annotation> ```env OPENAI_API_KEY=your_openai_api_key

Build and start the containers:
docker-compose up --build


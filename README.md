# End-To-End RAG System

This project is a skeleton for an End-To-End Retrieval-Augmented Generation (RAG) system built with Python and FastAPI. It provides a structured foundation for developing RAG applications using OpenAI or Gemini APIs.

## Prerequisites

- **Python**: Version 3.8

## Installation Guide

### 1. Install Miniconda

Miniconda is a minimal installer for Conda. It allows you to easily manage your Python environments and dependencies.

**Windows:**
1.  Download the Miniconda installer for Windows from the [official website](https://docs.conda.io/en/latest/miniconda.html#windows-installers).
2.  Run the `.exe` file.
3.  Follow the installation prompts.
4.  **Important:** When asked, it is recommended to check "Add Miniconda3 to my PATH environment variable" (or use the Anaconda Prompt to run commands).

**macOS:**
1.  Download the Miniconda installer for macOS (pkg or bash installer) from the [official website](https://docs.conda.io/en/latest/miniconda.html#macos-installers).
2.  Run the installer and follow the instructions.

**Linux:**
1.  Download the installer:
    ```bash
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    ```
2.  Run the installer:
    ```bash
    bash Miniconda3-latest-Linux-x86_64.sh
    ```

### 2. Create a Conda Environment

Once Miniconda is installed, open your terminal (or Anaconda Prompt on Windows) and create a new environment with Python 3.8:

```bash
conda create -n rag-system python=3.8 -y
```

Activate the environment:

```bash
conda activate rag-system
```

### 3. Install Dependencies

Navigate to the project root directory and install the required Python packages:

```bash
pip install -r requirements.txt
```

## Configuration

1.  Navigate to the `src` directory.
2.  Copy the example environment file:
    ```bash
    cp .env.example .env
    # On Windows Command Prompt: copy .env.example .env
    ```
3.  Open `.env` and add your API keys:
    ```ini
    APP_NAME="RAG-SYSTEM"
    VERSION="1.0.0"
    OPENAI_API_KEY="your_openai_api_key"
    GEMINI_API_KEY="your_gemini_api_key"
    FILE_ALLOWED_EXTENSIONS=["image/jpeg","image/png","text/plain","application/pdf"]
    FILE_MAX_SIZE=10485760 # 10 MB
    FILE_DEFUALT_CHUNK_SIZE=512000 # 500 KB
    ```

## Project Structure

```
End-To-End-RAG-System/
├── src/
│   ├── assets/         # Static assets
│   ├── controller/     # API route controllers
│   ├── models/         # Data models and schemas
│   ├── routers/        # API routers
│   ├── main.py         # Application entry point
│   └── .env            # Environment variables
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Running the Application

To start the FastAPI server, run the following command from the root directory:

```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`. You can access the interactive API docs at `http://localhost:8000/docs`.

## Features

- **File Upload**: Upload files to specific projects with validation for file type and size.
- **Project Management**: (In progress) Structure for managing project-specific files.

## API Endpoints

### Base
- `GET /Base/welcome`: Health check endpoint returning app name and version.

### Data
- `POST /Data/upload_file/{project_id}`: Upload a file to a specific project.
    - **Path Parameters**: `project_id` (string)
    - **Body**: `file` (UploadFile)
    - **Returns**: JSON response with file details and status.

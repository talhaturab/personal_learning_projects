# FastNotes API

## Overview

FastNotes is a simple yet powerful API built using FastAPI that allows users to perform CRUD operations (Create, Read, Update, Delete) on notes. The notes are stored in a MongoDB database, providing a scalable and efficient solution for managing your notes.

## Features

- **Create Note**: Easily create new notes by sending a POST request to the API.

- **Read Note**: Retrieve notes by sending a GET request. You can filter notes based on importance.

- **Update Note**: Modify existing notes, including updating the importance status.

- **Delete Note**: Remove unwanted notes using a DELETE request.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or later
- MongoDB

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fastnotes-api.git
   ```

2. Install dependencies:

   ```bash
   cd fastnotes-api
   pip install -r requirements.txt
   ```

3. Configure MongoDB:

   Update the `config.py` file with your MongoDB connection details.

4. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

   The API will be accessible at `http://localhost:8000`.

## Usage

### Create a Note

Send a POST request to `http://localhost:8000/notes/` with the following JSON payload:

```json
{
  "title": "My Important Note",
  "content": "This is the content of my note.",
  "important": true
}
```

### Read Notes

Send a GET request to `http://localhost:8000/notes/` to retrieve all notes. You can also filter notes based on importance:

- All notes: `http://localhost:8000/notes/`
- Important notes: `http://localhost:8000/notes/?important=true`
- Non-important notes: `http://localhost:8000/notes/?important=false`

### Update a Note

Send a PUT request to `http://localhost:8000/notes/{note_id}` with the updated JSON payload.

### Delete a Note

Send a DELETE request to `http://localhost:8000/notes/{note_id}` to delete a specific note.

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy noting! 📝✨

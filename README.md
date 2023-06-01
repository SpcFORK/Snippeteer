# Code Snippet API

This is a simple API that allows users to upload code snippets, view all snippets, upvote them, and filter them based on language, creation date, or likes.

## Prerequisites

- Python 3.x
- Flask framework
- SQLite

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/code-snippet-api.git
```

2. Install the required dependencies:

```bash
pip install flask
```

3. Initialize the SQLite database:

```bash
python initialize_database.py
```

## Usage

1. Start the API server:

```bash
python api.py
```

2. Interact with the API using tools like cURL or Postman.

- Uploading a code snippet:
  - URL: `POST /snippets`
  - Payload:
    ```json
    {
      "code": "your code here",
      "language": "python"
    }
    ```

- Viewing all snippets:
  - URL: `GET /snippets`

- Upvoting a snippet:
  - URL: `PUT /snippets/{snippet_id}/like`

- Filtering snippets:
  - URL: `GET /snippets/filter`
  - Query Parameters:
    - `language`: Filter by programming language
    - `created_at`: Filter by creation date (in the format YYYY-MM-DD)
    - `likes`: Filter by minimum number of likes

## Database Schema

The code snippets are stored in an SQLite database with the following schema:

```sql
CREATE TABLE snippets (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL,
  language TEXT NOT NULL,
  created_at TEXT NOT NULL,
  likes INTEGER NOT NULL DEFAULT 0
);
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE.txt).
# Flask Service ReadMe

## Overview

This is a simple Flask-based API that handles POST requests. The service receives a JSON payload containing a numeric input, calculates the floor of the number, and returns the result.

docker image url

https://hub.docker.com/r/emirob/emi-repo/tags

docker pull command

```bash
docker pull emirob/emi-repo
```

## Requirements

To run this application, ensure you have the following:

- Python 3.x
- Flask

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required Python dependencies:

   ```bash
   pip install flask
   ```

3. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Running the Application

### Development Mode

To run the application in development mode:

1. Export the Flask app environment variable:

   ```bash
   export FLASK_APP=app.py  # On Windows: set FLASK_APP=app.py
   ```

2. Run the Flask server:
   ```bash
   flask run
   ```

### Production Mode

To run the application in production mode with Gunicorn:

1. Install Gunicorn:

   ```bash
   pip install gunicorn
   ```

2. Run Gunicorn:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8080 app:app
   ```

## API Usage

### Endpoint

`POST /`

### Request

Send a JSON payload with the following structure:

```json
{
  "input": <numeric-value>
}
```

### Response

The API returns the floored value of the input number as a string.

#### Example Request

```bash
curl -X POST http://localhost:8080/ \
    -H "Content-Type: application/json" \
    -d '{"input": 5.8}'
```

#### Example Response

```
"5"
```

### Error Handling

The API expects a valid JSON payload with a key `input` containing a numeric value. If the payload is malformed or `input` is missing, the API will respond with an error.

## Logging

The application redirects logs to Gunicorn when run in production mode. Log messages include service start information and other runtime details.

## Environment Variables

- `PORT`: Specifies the port number the Flask app will run on (default: 8080).

## Notes

- Ensure that you have properly set up logging when deploying with Gunicorn.

---

Emi Roberti - Happy coding

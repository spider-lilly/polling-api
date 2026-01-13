# Polling API

A simple REST API for handling realtime polling system using Flask + PostgreSQL.

## Installation

### 1. Clone repo

```bash
git clone https://github.com/spider-lilly/polling-api.git
cd polling-api
```

### 2. Setup virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup `.env`

```ini
DATABASE_URL=YOUR_DATABASE_URL
```

### 5. Run app

```bash
python run.py
```

API will be available at:
**[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

## API Endpoints

### Add User

`POST /register`

#### Example

**Request**

```http
POST /register
Content-Type: application/json
```

```json
{
  "user_id": "john_doe",
  "password": "securepass123"
}
```

**Response**

```json
{
  "message": "User registered successfully"
}
```

### Add Poll

`POST /polls`

#### Example

**Request**

```http
POST /polls
Content-Type: application/json
```

```json
{
  "question": "anyone there?",
  "options": ["no", "yes"]
}
```

**Response**

```json
{
  "message": "Poll created successfully",
  "poll_id": 1
}
```

### Get Poll Data

`GET /polls/<poll_id>`

#### Example

**Request**

```http
GET /polls/1
```

**Response**

```json
{
  "closes": "2026-01-14T04:57:31.669656",
  "is_closed": false,
  "options": [
    {
      "option_id": 1,
      "option_text": "no",
      "votes": 0
    },
    {
      "option_id": 2,
      "option_text": "yes",
      "votes": 3
    }
  ],
  "poll_id": 1,
  "question": "anyone there?"
}
```

### Cast Vote

`POST /polls/<poll_id>/vote`

#### Example

**Request**

```http
POST /polls/1/vote
Content-Type: application/json
```

```json
{
  "user_id": "john_doe",
  "password": "securepass123",
  "option": "yes"
}
```

**Response**

```json
{
  "message": "vote recorded"
}
```

## One Vote Per User Logic

This application uses a database-level unique constraint on `(poll_id, user_id)` which ensures each user can only vote once per poll. When a user attempts to vote, the system:

1. Authenticates the user's credentials
2. Attempts to insert a new vote record into the database
3. If the user has already voted on that poll, the database constraint prevents the duplicate entry and raises an exception
4. The exception is caught and returns an error message: "user has already voted"

This is how the application prevents users from casting multiple votes on the same poll, maintaining the integrity of the voting results.

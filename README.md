# 🎤 Late Show API

This is a Flask-based REST API that simulates a TV show appearance tracker. The app allows you to view episodes, guests, and manage appearances — with proper model relationships, validations, and JSON responses.

## 📁 Project Structure

```
lateshow-alvin-makaya/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── seed.py
├── seed.csv
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/your-username/lateshow-alvin-makaya.git
cd lateshow-alvin-makaya
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Initialize the Database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 3. Seed the Database

```bash
python app/seed.py
```

### 4. Run the App

```bash
python app.py
```

Visit `http://localhost:5555` to get started.

---

## 🧠 Models

- **Episode**
  - `id`, `date`, `number`
- **Guest**
  - `id`, `name`, `occupation`
- **Appearance**
  - `id`, `rating`, `episode_id`, `guest_id`

**Relationships:**

- `Episode` has many `Guest`s through `Appearance`
- `Guest` has many `Episode`s through `Appearance`

**Validation:**

- `Appearance.rating` must be between 1 and 5 (inclusive)

---

## 🛣️ API Endpoints

### `GET /episodes`

Returns a list of all episodes.

### `GET /episodes/<int:id>`

Returns one episode and its appearances.

### `GET /guests`

Returns a list of all guests.

### `POST /appearances`

Creates a new appearance (with validation).

**Request JSON:**

```json
{
  "rating": 5,
  "episode_id": 2,
  "guest_id": 3
}
```

**Response JSON:**

```json
{
  "id": 162,
  "rating": 5,
  "guest_id": 3,
  "episode_id": 2,
  "episode": {
    "date": "1/12/99",
    "id": 2,
    "number": 2
  },
  "guest": {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
}
```

---

## 🧪 Testing

Use the provided [Postman collection](./challenge-4-lateshow.postman_collection.json) to test all endpoints. Import the collection into Postman and hit `localhost:5555`.

---

## ✅ Done By

**Alvin Amisi Makaya**  
Phase 4 Code Challenge  
Moringa School

---

## 📝 Notes

- Validation errors return a JSON response with `errors` and appropriate status codes.
- Relationships are configured with cascading deletes to maintain DB integrity.
- Project uses SQLite for simplicity, easily switchable to PostgreSQL.

---

```

```

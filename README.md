# Language Learning Portal API

## Project Overview 🎉

This is my implementation of the language learning portal API for Professor Brown's GenAI Bootcamp 2025. The API helps track study sessions and word reviews for learning Japanese.

### What It Does
- Creates study sessions
- Records word reviews
- Shows Japanese words with translations
- Breaks down words into parts (kanji/hiragana)

## How to Run It 🚀

1. Install what you need:

```bash
pip install flask flask-sqlalchemy flask-migrate flask-cors python-dotenv
``` 


2. Set up the database:

```bash
flask --app lang_portal.wsgi:app db init
flask --app lang_portal.wsgi:app db migrate
flask --app lang_portal.wsgi:app db upgrade
```

3. Add test data:
```
python -m lang_portal.seed
```

4. Start the server:
```
flask --app lang_portal.wsgi:app run --debug --port=5001
```

## API Endpoints I Added 🛣️

1. Create Study Session:

POST /study_sessions
Content-Type: application/json

{
    "group_id": 1,
    "study_activity_id": 1
}

2. Add Review:

POST /study_sessions/<id>/review
Content-Type: application/json

{
    "word_id": 1,
    "correct": true
}

3. Get Words:

GET /groups/<id>/words/raw

Each endpoint helps:
- Track study progress
- Record word reviews
- Show Japanese words with translations

## Testing It Out 🧪

1. Open in browser:
```
http://localhost:5001/test
```

2. Try the buttons to:
   - Create study sessions
   - Add reviews
   - View words

## What I Learned 📚

- Built my first Flask API
- Worked with databases
- Fixed different types of errors
- *Used Claude (AI Assistant) for help*
- Created and tested API endpoints

## Problems I Fixed 🐛

1. **Module Not Found Error**
   - Changed folder name to use underscore
   - Python doesn't like hyphens!

2. **Access Denied Error**
   - Added CORS settings
   - Made API accessible

3. **Port 5000 Problems**
   - MacOS was using port 5000
   - Switched to port 5001

4. **Database Issues**
   - Had to run migrations
   - Added test data

## Quick Fixes 🔧

If server won't start:
```
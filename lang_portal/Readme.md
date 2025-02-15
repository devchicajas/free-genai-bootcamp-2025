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

### Watch How It Works! 📺
Here's me testing out the API:

<video width="640" height="360" controls>
  <source src="https://github.com/devchicajas/free-genai-bootcamp-2025/blob/af429d35c5f4d71e7e19bfa85aea3c2572233193/docs/videos/apiendpoint.mp4" type="video/mp4">
</video>

*The test page makes it super easy to try everything out - no complicated API tools needed!*

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

```bash
# This helped me when the server wouldn't start!
lsof -i :5001  # Shows what's using port 5001
kill -9 <PID>  # Stops whatever's blocking our port

# If database is acting weird, this usually helps:
rm -f instance/lang_portal.db
flask --app lang_portal.wsgi:app db upgrade
python -m lang_portal.seed  # Adds the test data back
```

## Stuff That Broke (And How I Fixed It!) 🔥

1. **My Imports Kept Breaking**
   - I kept getting `ModuleNotFoundError` 
   - Turns out I needed to add `lang_portal` to my imports!
   ```python
   # This didn't work:
   from models.word import Word
   
   # This worked!
   from lang_portal.models.word import Word
   ```

2. **Japanese Text Was Coming Out Weird**
   - All my Japanese characters were showing as \u3042 stuff
   - Fixed it by adding this to my Flask app:
   ```python
   app.json.ensure_ascii = False  # Makes Japanese show up properly!
   ```

3. **Frontend Couldn't Talk to Backend**
   - Got a bunch of CORS errors in console
   - Added this and it worked:
   ```python
   CORS(app, resources={
       r"/*": {"origins": ["http://localhost:3000"]}
   })
   ```

4. **Database Kept Disappearing**
   - Had to create an `instance` folder first
   - This command saved me:
   ```bash
   mkdir instance
   ```

## Cool Things I Learned 🌟

1. **Working With Japanese Text**
   - Always use UTF-8 (learned this the hard way!)
   - Add this at the top of Python files:
   ```python
   # -*- coding: utf-8 -*-
   ```

2. **Testing The API**
   - Used Postman a lot
   - But this curl command is handy too:
   ```bash
   curl -X POST http://localhost:5001/study_sessions \
        -H "Content-Type: application/json" \
        -d '{"group_id": 1, "study_activity_id": 1}'
   ```

## When Things Break 😅

If something's not working:
1. Check `instance/lang_portal.log` (helped me debug a lot!)
2. Make sure you're in your virtual environment
3. Try running with debug mode:
   ```bash
   FLASK_DEBUG=1 flask --app lang_portal.wsgi:app run --port=5001
   ```

## Stuff You Need to Run This 🛠️

- Python (I'm using 3.8)
- Flask
- A way to handle Japanese text
- That's pretty much it!

## What I Want to Add Next 🚀

1. User login (once I figure out authentication!)
2. More Japanese features:
   - How to write kanji
   - How to pronounce words
   - Example sentences
3. Better stats about study sessions
4. Maybe export study data to Excel?

## Thank You! 🙏

- Claude (saved me from many debugging nightmares)
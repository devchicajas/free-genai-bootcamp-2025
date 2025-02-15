from lang_portal import create_app, db
from lang_portal.models import Group, Word, WordPart, StudyActivity

def seed_database():
    app = create_app()
    with app.app_context():
        # Create a study activity
        activity = StudyActivity(
            name="Flashcards",
            url="/study/flashcards",
            preview_url="/preview/flashcards"
        )
        db.session.add(activity)

        # Create a group
        group = Group(name="Basic Japanese")
        db.session.add(group)
        
        # Create some words
        word1 = Word(
            text="食べる",
            translation="to eat",
            group=group
        )
        db.session.add(word1)
        
        # Add word parts
        part1 = WordPart(
            word=word1,
            text="食",
            translation="eat",
            part_of_speech="kanji"
        )
        part2 = WordPart(
            word=word1,
            text="べる",
            translation=None,
            part_of_speech="hiragana"
        )
        db.session.add(part1)
        db.session.add(part2)
        
        db.session.commit()

if __name__ == '__main__':
    seed_database() 
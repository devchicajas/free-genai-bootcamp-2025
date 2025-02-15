from flask import Blueprint, request, jsonify, render_template
from flask_cors import cross_origin
from datetime import datetime
from lang_portal.models import db, StudySession, StudySessionReview, Word, WordPart, Group, StudyActivity

bp = Blueprint('main', __name__, template_folder='templates')

# Route to serve our testing interface
@bp.route('/test')
def test_page():
    return render_template('test.html')

# Create a new study session when user starts studying
@bp.route('/study_sessions', methods=['POST'])
@cross_origin()
def create_study_session():
    # Get the JSON data sent from the frontend
    data = request.get_json()
    
    try:
        # Create a new study session record in the database
        new_session = StudySession(
            group_id=data['group_id'],          # Which word group to study
            study_activity_id=data['study_activity_id']  # What type of study activity
        )
        
        # Save to database
        db.session.add(new_session)
        db.session.commit()
        
        # Return the created session details
        return jsonify({
            'id': new_session.id,
            'group_id': new_session.group_id,
            'study_activity_id': new_session.study_activity_id,
            'created_at': new_session.created_at.isoformat()
        }), 201  # 201 means "Created"
        
    except Exception as e:
        # If anything goes wrong, undo database changes
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Record a review result when user answers a word
@bp.route('/study_sessions/<int:id>/review', methods=['POST'])
@cross_origin()
def add_session_review(id):
    # Get the JSON data sent from the frontend
    data = request.get_json()
    
    try:
        # Create a new review record
        review = StudySessionReview(
            session_id=id,                # Which study session this belongs to
            word_id=data['word_id'],     # Which word was reviewed
            correct=data['correct']       # Whether user got it right
        )
        
        # Save to database
        db.session.add(review)
        db.session.commit()
        
        # Return the created review details
        return jsonify({
            'id': review.id,
            'session_id': review.session_id,
            'word_id': review.word_id,
            'correct': review.correct,
            'reviewed_at': review.reviewed_at.isoformat()
        }), 201
        
    except Exception as e:
        # If anything goes wrong, undo database changes
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Get all words and their parts for a specific group
@bp.route('/groups/<int:id>/words/raw', methods=['GET'])
@cross_origin()
def get_group_words_raw(id):
    try:
        # Get all words that belong to this group
        words = Word.query.filter_by(group_id=id).all()
        
        result = []
        for word in words:
            # For each word, get its component parts
            parts = WordPart.query.filter_by(word_id=word.id).all()
            
            # Build a complete word object with all its parts
            word_data = {
                'id': word.id,
                'text': word.text,              # The complete word
                'translation': word.translation, # English translation
                'group_id': word.group_id,
                'parts': [{                     # Break down into parts (like kanji/hiragana)
                    'id': part.id,
                    'text': part.text,
                    'translation': part.translation,
                    'part_of_speech': part.part_of_speech
                } for part in parts]
            }
            result.append(word_data)
            
        return jsonify(result), 200  # 200 means "OK"
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


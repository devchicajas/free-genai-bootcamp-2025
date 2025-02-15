from lang_portal import db
from datetime import datetime


class Group(db.Model):
    __tablename__ = 'groups'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    words = db.relationship('Word', backref='group', lazy=True)

class Word(db.Model):
    __tablename__ = 'words'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    translation = db.Column(db.String(200))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    parts = db.relationship('WordPart', backref='word', lazy=True)

class WordPart(db.Model):
    __tablename__ = 'word_parts'
    
    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'), nullable=False)
    text = db.Column(db.String(50), nullable=False)
    translation = db.Column(db.String(100))
    part_of_speech = db.Column(db.String(50))

class StudySession(db.Model):
    __tablename__ = 'study_sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    study_activity_id = db.Column(db.Integer, db.ForeignKey('study_activities.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Relationships
    group = db.relationship('Group', backref='study_sessions')
    study_activity = db.relationship('StudyActivity', backref='study_sessions')
    reviews = db.relationship('StudySessionReview', backref='session', lazy=True)

class StudySessionReview(db.Model):
    __tablename__ = 'study_session_reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('study_sessions.id'), nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'), nullable=False)
    correct = db.Column(db.Boolean, nullable=False)
    reviewed_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Relationships
    word = db.relationship('Word', backref='reviews')

class StudyActivity(db.Model):
    __tablename__ = 'study_activities'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    preview_url = db.Column(db.String(200)) 
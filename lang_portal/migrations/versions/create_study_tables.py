"""create study tables

Revision ID: [will be generated]
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create study_activities table
    op.create_table(
        'study_activities',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('url', sa.String(200), nullable=False),
        sa.Column('preview_url', sa.String(200)),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create study_sessions table
    op.create_table(
        'study_sessions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=False),
        sa.Column('study_activity_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['group_id'], ['groups.id']),
        sa.ForeignKeyConstraint(['study_activity_id'], ['study_activities.id']),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create study_session_reviews table
    op.create_table(
        'study_session_reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('session_id', sa.Integer(), nullable=False),
        sa.Column('word_id', sa.Integer(), nullable=False),
        sa.Column('correct', sa.Boolean(), nullable=False),
        sa.Column('reviewed_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['session_id'], ['study_sessions.id']),
        sa.ForeignKeyConstraint(['word_id'], ['words.id']),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('study_session_reviews')
    op.drop_table('study_sessions')
    op.drop_table('study_activities') 
"""initial_migration

Revision ID: 66266097d526
Revises: 
Create Date: 2021-11-15 18:25:13.494781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66266097d526'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('word', sa.String(length=100), nullable=False),
    sa.Column('phrase_tag', sa.String(length=2), nullable=False),
    sa.Column('context', sa.String(length=100), nullable=False),
    sa.Column('form_translation', sa.String(length=100), nullable=False),
    sa.Column('context_translation', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    op.drop_table('card')
    # ### end Alembic commands ###

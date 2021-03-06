"""game start/end

Revision ID: bdc94b8235db
Revises: 66266097d526
Create Date: 2021-11-15 21:29:45.320636

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bdc94b8235db'
down_revision = '66266097d526'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('started_at', sa.DateTime(), nullable=True))
    op.add_column('game', sa.Column('ended_at', sa.DateTime(), nullable=True))
    op.drop_column('game', 'player')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('player', mysql.VARCHAR(length=20), nullable=True))
    op.drop_column('game', 'ended_at')
    op.drop_column('game', 'started_at')
    # ### end Alembic commands ###

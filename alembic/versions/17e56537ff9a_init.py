"""init

Revision ID: 17e56537ff9a
Revises: 
Create Date: 2021-07-07 15:09:37.876759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17e56537ff9a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'todo',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=True),
        sa.Column('description', sa.String, nullable=True)
    )


def downgrade():
    op.drop_table('todo')

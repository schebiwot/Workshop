"""users

Revision ID: 871a42cf7efc
Revises: c08dcd37742a
Create Date: 2020-03-04 20:00:39.124186

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '871a42cf7efc'
down_revision = 'c08dcd37742a'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, unique=True, nullable=False, primary_key=True),
        sa.Column('name', sa.String(100), unique=False, nullable=False),
        sa.Column('username', sa.String(100), unique=False, nullable=False),
        sa.Column('email', sa.String(100), unique=False, nullable=False),
        sa.Column('password', sa.String(128), unique=False, nullable=False),
    )


def downgrade():
    op.drop_table('users')

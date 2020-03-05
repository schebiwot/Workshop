"""service

Revision ID: e89e92d767d6
Revises: f5ca6b605ed3
Create Date: 2020-03-04 16:53:05.436029

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e89e92d767d6'
down_revision = 'f5ca6b605ed3'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'service',
        sa.Column('id', sa.Integer, unique=True, nullable=False, primary_key=True),
        sa.Column('truck_id', sa.Integer, sa.ForeignKey('truck.id'))
    )


def downgrade():
    op.drop_table('service')

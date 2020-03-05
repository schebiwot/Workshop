"""service_items

Revision ID: 3250d17f8acc
Revises: e89e92d767d6
Create Date: 2020-03-04 16:53:14.675788

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '3250d17f8acc'
down_revision = 'e89e92d767d6'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'service_items',
        sa.Column('id', sa.Integer, unique=True, nullable=False, primary_key=True),
        sa.Column('service_id', sa.String(100), nullable=False),
        sa.Column('part_id', sa.String(100), unique=False, nullable=False),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('subtotal', sa.Numeric(10, 2), nullable=False),
        sa.Column('service_id', sa.Integer, sa.ForeignKey('service.id')),
    )


def downgrade():
    op.drop_table('service_items')

"""parts

Revision ID: f5ca6b605ed3
Revises: e3bb31af43db
Create Date: 2020-03-04 16:52:40.971132

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f5ca6b605ed3'
down_revision = 'e3bb31af43db'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'parts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('part_no', sa.String(100), unique=False, nullable=False),
        sa.Column('description', sa.String(100), unique=False, nullable=False),
        sa.Column('unit_price', sa.Numeric(10, 2), nullable=False),
        sa.Column('truck_model_id', sa.String(100), sa.ForeignKey('truck_model.model_no'), nullable=False),
    )


def downgrade():
    op.drop_table('parts')

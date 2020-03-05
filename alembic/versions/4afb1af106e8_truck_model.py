"""truck_model

Revision ID: 4afb1af106e8
Revises: 
Create Date: 2020-03-04 16:51:44.460395

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4afb1af106e8'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'truck_model',
        sa.Column('model_no', sa.String(100), unique=False, nullable=False, primary_key=True),
    )


def downgrade():
    op.drop_table('truck_model')

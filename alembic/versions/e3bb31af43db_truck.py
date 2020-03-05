"""truck

Revision ID: e3bb31af43db
Revises: 4afb1af106e8
Create Date: 2020-03-04 16:52:12.939627

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e3bb31af43db'
down_revision = '4afb1af106e8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'truck',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('driver_name', sa.String(100), nullable=False),
        sa.Column('driver_Phone_number', sa.Integer, nullable=False),
        sa.Column('company_name', sa.String(100), nullable=False),
        sa.Column('owner_name', sa.String(100), nullable=False),
        sa.Column('owner_email', sa.String(100), unique=False, nullable=False),
        sa.Column('truck_model', sa.String(100), unique=False, nullable=False),
        sa.Column('registration', sa.String(100), unique=True, nullable=False),
        sa.Column('chassis', sa.String(100), unique=True, nullable=False),
        sa.Column('engine_number', sa.Integer, nullable=False),
        sa.Column('mileage', sa.Integer, nullable=False),
        sa.Column('technician', sa.Integer, sa.ForeignKey('users.id')),
    )


def downgrade():
    op.drop_table('truck')

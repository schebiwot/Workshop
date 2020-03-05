"""seed_parts

Revision ID: c08dcd37742a
Revises: 3250d17f8acc
Create Date: 2020-03-04 17:32:25.466900

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c08dcd37742a'
down_revision = '3250d17f8acc'
branch_labels = None
depends_on = None

from alembic import op
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date, Numeric


def upgrade():
    parts_table = table('parts',
                        column('truck_model_id', String),
                        column('part_no', String),
                        column('description', String),
                        column('unit_price', Numeric)
                        )
    truck_model_table = table('truck_model',
                              column('model_no', String)
                              )
    op.bulk_insert(truck_model_table,
                   [
                       {'model_no': 'MODEL DOST'},
                       {'model_no': 'MODEL PARTNER'},
                       {'model_no': 'MODEL 9016'},
                       {'model_no': 'MODEL2518'}
                   ]
                   )
    op.bulk_insert(parts_table,
                   [
                       {'truck_model_id': 'MODEL2518', 'part_no': 'F8835100', 'description': 'FUEL FILTER',
                        'unit_price': 3569.00},
                       {'truck_model_id': 'MODEL2518', 'part_no': 'F7A01500', 'description': 'OIL FILTER',
                        'unit_price': 4371.00},
                       {'truck_model_id': 'MODEL2518', 'part_no': 'F7B01100', 'description': 'AIR FILTER OUTER',
                        'unit_price': 6934.00},
                       {'truck_model_id': 'MODEL2518', 'part_no': 'F7B01200', 'description': 'AIR FILTER INNER',
                        'unit_price': 1759.00},
                       {'truck_model_id': 'MODEL2518', 'part_no': 'B1304301', 'description': 'CLUTCH PLATE',
                        'unit_price': 15929.00},
                       {'truck_model_id': 'MODEL2518', 'part_no': 'B1391801', 'description': 'PRESSURE PLATE',
                        'unit_price': 22248.00},
                       {'truck_model_id': 'MODEL 9016', 'part_no': 'F8835100', 'description': 'FUEL FILTER',
                        'unit_price': 2569.00},
                       {'truck_model_id': 'MODEL 9016', 'part_no': 'X4001000', 'description': 'OIL FILTER',
                        'unit_price': 737.00},
                       {'truck_model_id': 'MODEL 9016', 'part_no': 'X8806400', 'description': 'AIR FILTER OUTER',
                        'unit_price': 1241.00},
                       {'truck_model_id': 'MODEL 9016', 'part_no': 'X8806500', 'description': 'AIR FILTER INNER',
                        'unit_price': 5861.00},
                       {'truck_model_id': 'MODEL 9016', 'part_no': 'B1301407', 'description': 'CLUTCH PLATE',
                        'unit_price': 21707.00},
                       {'truck_model_id': 'MODEL 9016', 'part_no': 'B1301401', 'description': 'PRESSURE PLATE',
                        'unit_price': 36816.00},
                       {'truck_model_id': 'MODEL PARTNER', 'part_no': '164032VB1A', 'description': 'FUEL FILTER',
                        'unit_price': 3856.00},
                       {'truck_model_id': 'MODEL PARTNER', 'part_no': '152092VB0A', 'description': 'OIL FILTER',
                        'unit_price': 1179.00},
                       {'truck_model_id': 'MODEL PARTNER', 'part_no': '165462VE0A', 'description': 'AIR FILTER OUTER',
                        'unit_price': 7145.00},
                       {'truck_model_id': 'MODEL PARTNER', 'part_no': '3010002VE0A', 'description': 'CLUTCH PLATE',
                        'unit_price': 9376.00},
                       {'truck_model_id': 'MODEL PARTNER', 'part_no': '302102VE0A', 'description': 'PRESSURE PLATE',
                        'unit_price': 9453.00},
                       {'truck_model_id': 'MODEL DOST', 'part_no': 'F7A00180 ', 'description': 'FUEL FILTER',
                        'unit_price': 661.00},
                       {'truck_model_id': 'MODEL DOST', 'part_no': 'F7A00170', 'description': 'OIL FILTER',
                        'unit_price': 2242.00},
                       {'truck_model_id': 'MODEL DOST', 'part_no': '165462VA1A', 'description': 'AIR FILTER OUTER',
                        'unit_price': 1793.00},
                       {'truck_model_id': 'MODEL DOST', 'part_no': '301002VA1A ', 'description': 'CLUTCH PLATE',
                        'unit_price': 4313.00},
                       {'truck_model_id': 'MODEL DOST', 'part_no': '302102VA1A', 'description': 'PRESSURE PLATE',
                        'unit_price': 3683.00}
                   ]
                   )


def downgrade():
    pass

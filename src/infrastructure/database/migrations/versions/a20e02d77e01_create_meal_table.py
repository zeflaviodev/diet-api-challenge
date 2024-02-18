#pylint: disable=no-member
"""create meal table

Revision ID: a20e02d77e01
Revises: 
Create Date: 2024-02-18 18:21:22.102045

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a20e02d77e01'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'meals',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('description', sa.String(300), nullable=False),
        sa.Column('meal_at', sa.DateTime, nullable=False),
        sa.Column('in_diet', sa.Boolean, nullable=False, default=True)
    )


def downgrade() -> None:
    op.drop_table('meals')

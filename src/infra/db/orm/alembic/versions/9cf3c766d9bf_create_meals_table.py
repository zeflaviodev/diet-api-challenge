#pylint:disable=no-member,invalid-name
"""create meals table

Revision ID: 9cf3c766d9bf
Revises: 
Create Date: 2024-03-02 12:38:04.553718

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9cf3c766d9bf'
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

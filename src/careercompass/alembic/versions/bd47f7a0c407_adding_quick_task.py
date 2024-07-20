"""Adding Quick Task

Revision ID: bd47f7a0c407
Revises: 43ab870a0476
Create Date: 2024-07-20 14:49:39.306864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = 'bd47f7a0c407'
down_revision: Union[str, None] = '43ab870a0476'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('quicktasks',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('quicktasks')
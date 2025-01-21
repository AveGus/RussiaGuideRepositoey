"""empty message

Revision ID: a09398b31d92
Revises: 8113b748b8f3
Create Date: 2024-11-23 04:49:52.437139

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a09398b31d92'
down_revision: Union[str, None] = '8113b748b8f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

"""empty message

Revision ID: 0310d9969598
Revises: 743c2641d145
Create Date: 2024-11-23 04:57:00.329573

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0310d9969598'
down_revision: Union[str, None] = '743c2641d145'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

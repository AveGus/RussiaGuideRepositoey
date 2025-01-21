"""empty message

Revision ID: 102ff5ba0bf3
Revises: 7a17d62acd2d
Create Date: 2024-11-23 04:53:21.875327

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '102ff5ba0bf3'
down_revision: Union[str, None] = '7a17d62acd2d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

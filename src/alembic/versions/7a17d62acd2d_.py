"""empty message

Revision ID: 7a17d62acd2d
Revises: a09398b31d92
Create Date: 2024-11-23 04:53:15.104516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a17d62acd2d'
down_revision: Union[str, None] = 'a09398b31d92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

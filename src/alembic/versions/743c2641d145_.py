"""empty message

Revision ID: 743c2641d145
Revises: 102ff5ba0bf3
Create Date: 2024-11-23 04:55:20.875425

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '743c2641d145'
down_revision: Union[str, None] = '102ff5ba0bf3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

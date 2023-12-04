"""Add Role class with enum

Revision ID: 0a3c188678e9
Revises: b8bca04e9e16
Create Date: 2023-11-28 18:34:37.374294

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
# from sqlalchemy import Enum
# from app.models.task import Role
# revision identifiers, used by Alembic.
revision: str = '0a3c188678e9'
down_revision: Union[str, None] = 'b8bca04e9e16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# class Role(sa.Enum):
#     pass

def upgrade() -> None:

    role_enum = sa.Enum('admin', 'manager', 'employee', name='role_enum')
    role_enum.create(op.get_bind(), checkfirst=False)
    # op.add_column('users', sa.Column('role', role_enum, nullable=False))
   
  


def downgrade() -> None:
    op.drop_column('users')

    role_enum = sa.Enum('admin', 'manager', 'employee', name='role_enum')
    role_enum.drop(op.get_bind(), checkfirst=False)
   


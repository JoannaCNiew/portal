"""rename users table to authors

Revision ID: 4b94e90df8a5
Revises: 713648c79898
Create Date: 2023-03-22 18:55:09.293723

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4b94e90df8a5'
down_revision = '713648c79898'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('users', 'authors')

def downgrade() -> None:
    op.rename_table('authors', 'users')



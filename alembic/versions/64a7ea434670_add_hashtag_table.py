"""add hashtag table

Revision ID: 64a7ea434670
Revises: 9244604d4754
Create Date: 2023-03-22 18:36:15.120564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64a7ea434670'
down_revision = '9244604d4754'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hashtags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hashtags')
    # ### end Alembic commands ###

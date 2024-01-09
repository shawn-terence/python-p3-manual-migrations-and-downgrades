"""Altering tablename

Revision ID: 24659a06c57f
Revises: cac3ade677e3
Create Date: 2024-01-09 10:07:34.053714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24659a06c57f'
down_revision = 'cac3ade677e3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'email', new_column_name='Email_Address')


def downgrade() -> None:
    pass

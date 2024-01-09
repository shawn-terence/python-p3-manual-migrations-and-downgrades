"""Renaming students to scholars

Revision ID: cac3ade677e3
Revises: 791279dd0760
Create Date: 2024-01-09 09:50:44.410061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cac3ade677e3'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')

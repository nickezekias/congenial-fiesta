"""create_company_types_table

Revision ID: daf8f3d5ad8a
Revises: 1c9940a246df
Create Date: 2023-01-12 05:46:36.884246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daf8f3d5ad8a'
down_revision = '1c9940a246df'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'company_types',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name")
    )


def downgrade() -> None:
    op.drop_table('company_types')

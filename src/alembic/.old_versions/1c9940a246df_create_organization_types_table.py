"""create_organization_types_table

Revision ID: 1c9940a246df
Revises: 0517e030bf85
Create Date: 2023-01-12 05:44:30.189691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c9940a246df'
down_revision = '0517e030bf85'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'organization_types',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name")
    )


def downgrade() -> None:
    op.drop_table('organization_types')

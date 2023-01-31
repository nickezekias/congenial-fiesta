"""create_industries_table

Revision ID: 800576e45db4
Revises: c49bbe6d94ee
Create Date: 2023-01-12 05:29:08.568118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '800576e45db4'
down_revision = 'c49bbe6d94ee'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'industries',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name")
    )


def downgrade() -> None:
    op.drop_table('industries')

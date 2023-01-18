"""create_sectors_table

Revision ID: 0517e030bf85
Revises: 800576e45db4
Create Date: 2023-01-12 05:33:44.168768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0517e030bf85'
down_revision = '800576e45db4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'sectors',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name")
    )


def downgrade() -> None:
    op.drop_table('sectors')

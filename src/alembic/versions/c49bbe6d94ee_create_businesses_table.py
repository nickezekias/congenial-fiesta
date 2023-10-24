"""create_businesses_table

Revision ID: c49bbe6d94ee
Revises: 1e3f6c10836f
Create Date: 2023-01-12 03:05:10.756724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c49bbe6d94ee'
down_revision = '1e3f6c10836f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'businesses',
        sa.Column('id', sa.CHAR(36), primary_key=True, nullable=False),
        sa.Column('annual_turnover', sa.String(30), nullable=True),
        sa.Column('business_model', sa.String(255), nullable=True),
        sa.Column('company_size', sa.String(15), nullable=False),
        sa.Column('company_type', sa.String(30), nullable=False),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('employees', sa.String(255), nullable=True),
        sa.Column('ID_document', sa.String(255), nullable=True),
        sa.Column('ID_document_verified_at', sa.DateTime, nullable=True),
        sa.Column('industry', sa.String(30), nullable=False),
        sa.Column('investors', sa.String(255), nullable=True),
        sa.Column('locations', sa.String(255), nullable=True),
        sa.Column('markets', sa.String(255), nullable=True),
        sa.Column('name', sa.String(30), nullable=False),
        sa.Column('org_type', sa.String(30), nullable=False),
        sa.Column('partners', sa.String(255), nullable=True),
        sa.Column('payment', sa.String(255), nullable=True),
        sa.Column('payment_verified_at', sa.DateTime, nullable=True),
        sa.Column('pitch_deck', sa.String(255), nullable=True),
        sa.Column('products', sa.String(255), nullable=True),
        sa.Column('projects', sa.String(255), nullable=True),
        sa.Column('sector', sa.String(30), nullable=False),
        sa.Column('website', sa.Text, nullable=True),
        sa.Column('workspace', sa.JSON, nullable=False),
        sa.Column('year_founded', sa.DateTime, nullable=True),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f("ix_business_id"), "businesses", ["id"], unique=False)


def downgrade() -> None:
    op.drop_table('businesses')

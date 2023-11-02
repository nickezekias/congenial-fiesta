"""create_users_table

Revision ID: 1e3f6c10836f
Revises: d382efe64536
Create Date: 2023-01-09 18:56:05.834978

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1e3f6c10836f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.CHAR(36), primary_key=True, nullable=False),
        sa.Column('avatar', sa.String(255), nullable=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(30), unique=True, nullable=False),
        sa.Column('phone', sa.String(30), unique=True, nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('token', sa.String(255), unique=True, nullable=True),
        sa.Column('email_verified_at', sa.DateTime, nullable=True),
        sa.Column('phone_verified_at', sa.DateTime, nullable=True),
        sa.Column('ID_document', sa.String(255), nullable=True),
        sa.Column('ID_document_verified_at', sa.DateTime, nullable=True),
        sa.Column("is_active", sa.Boolean, nullable=False, default=0),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "users", ["email"], unique=True)
    op.create_index(op.f("ix_user_id"), "users", ["id"], unique=True)


def downgrade() -> None:
    op.drop_table('users')
 
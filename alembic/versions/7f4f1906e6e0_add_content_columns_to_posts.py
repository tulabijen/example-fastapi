"""add content columns to posts

Revision ID: 7f4f1906e6e0
Revises: c8458f625e36
Create Date: 2021-12-02 22:18:26.751145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f4f1906e6e0'
down_revision = 'c8458f625e36'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')

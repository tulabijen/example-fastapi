"""add more columns to post table

Revision ID: 65a250248d20
Revises: 7b7a3978150d
Create Date: 2021-12-02 22:25:50.001360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65a250248d20'
down_revision = '7b7a3978150d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='True'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')), )


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')

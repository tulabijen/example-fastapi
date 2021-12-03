"""add foreign key to post table

Revision ID: 7b7a3978150d
Revises: f8167b617cfa
Create Date: 2021-12-02 22:23:48.978659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b7a3978150d'
down_revision = 'f8167b617cfa'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')

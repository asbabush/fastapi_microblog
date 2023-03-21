"""Tree

Revision ID: 0e440d64ecad
Revises: e6c877b93f87
Create Date: 2023-03-21 22:25:07.685360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e440d64ecad'
down_revision = 'e6c877b93f87'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('microblog_posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('text', sa.String(length=350), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_microblog_posts_id'), 'microblog_posts', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_microblog_posts_id'), table_name='microblog_posts')
    op.drop_table('microblog_posts')
    # ### end Alembic commands ###

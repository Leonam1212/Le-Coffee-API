"""empty message

Revision ID: 71a85abd8df9
Revises: e131fdf0ea08
Create Date: 2022-03-04 15:17:39.048008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71a85abd8df9'
down_revision = 'e131fdf0ea08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###

"""''

Revision ID: 8bfe236bc74f
Revises: 8d0967ebc8e1
Create Date: 2020-06-30 19:11:33.152954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bfe236bc74f'
down_revision = '8d0967ebc8e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('pname', table_name='product')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('pname', 'product', ['pname'], unique=True)
    # ### end Alembic commands ###

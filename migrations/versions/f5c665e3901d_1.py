"""1

Revision ID: f5c665e3901d
Revises: 76261982be6d
Create Date: 2020-10-21 19:49:07.008685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5c665e3901d'
down_revision = '76261982be6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_official_user_official_userID'), 'official_user', ['official_userID'], unique=False)
    op.drop_index('ix_official_user_oid', table_name='official_user')
    op.create_index(op.f('ix_product_itemID'), 'product', ['itemID'], unique=False)
    op.drop_index('ix_product_pid', table_name='product')
    op.create_index(op.f('ix_type_typeID'), 'type', ['typeID'], unique=False)
    op.drop_index('ix_type_typeid', table_name='type')
    op.create_index(op.f('ix_user_userID'), 'user', ['userID'], unique=False)
    op.drop_index('ix_user_uid', table_name='user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_user_uid', 'user', ['userID'], unique=False)
    op.drop_index(op.f('ix_user_userID'), table_name='user')
    op.create_index('ix_type_typeid', 'type', ['typeID'], unique=False)
    op.drop_index(op.f('ix_type_typeID'), table_name='type')
    op.create_index('ix_product_pid', 'product', ['itemID'], unique=False)
    op.drop_index(op.f('ix_product_itemID'), table_name='product')
    op.create_index('ix_official_user_oid', 'official_user', ['official_userID'], unique=False)
    op.drop_index(op.f('ix_official_user_official_userID'), table_name='official_user')
    # ### end Alembic commands ###
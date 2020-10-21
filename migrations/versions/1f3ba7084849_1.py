"""1

Revision ID: 1f3ba7084849
Revises: f7b4e34e4b3a
Create Date: 2020-10-21 19:03:05.029529

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1f3ba7084849'
down_revision = 'f7b4e34e4b3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('all_order',
    sa.Column('orderID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('oPrice', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oDate', sa.DateTime(), nullable=True),
    sa.Column('address', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('orderID')
    )
    op.create_index(op.f('ix_all_order_orderID'), 'all_order', ['orderID'], unique=False)
    op.drop_index('ix_order_orderid', table_name='order')
    op.drop_table('order')
    op.add_column('cart', sa.Column('cNumber', sa.Integer(), nullable=True))
    op.add_column('cart', sa.Column('cPrice', mysql.DOUBLE(asdecimal=True), nullable=True))
    op.add_column('cart', sa.Column('cartID', sa.Integer(), autoincrement=True, nullable=False))
    op.create_index(op.f('ix_cart_cartID'), 'cart', ['cartID'], unique=False)
    op.drop_index('ix_cart_cid', table_name='cart')
    op.drop_constraint('cart_ibfk_2', 'cart', type_='foreignkey')
    op.drop_constraint('cart_ibfk_1', 'cart', type_='foreignkey')
    op.drop_column('cart', 'cid')
    op.drop_column('cart', 'pid')
    op.drop_column('cart', 'cnumber')
    op.drop_column('cart', 'cprice')
    op.drop_column('cart', 'uid')
    op.add_column('detailed_order', sa.Column('dPrice', mysql.DOUBLE(asdecimal=True), nullable=True))
    op.add_column('detailed_order', sa.Column('detailed_orderID', sa.Integer(), autoincrement=True, nullable=False))
    op.add_column('detailed_order', sa.Column('iNumber', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_detailed_order_detailed_orderID'), 'detailed_order', ['detailed_orderID'], unique=False)
    op.drop_index('ix_detailed_order_detailedoid', table_name='detailed_order')
    op.drop_constraint('detailed_order_ibfk_4', 'detailed_order', type_='foreignkey')
    op.drop_constraint('detailed_order_ibfk_3', 'detailed_order', type_='foreignkey')
    op.drop_constraint('detailed_order_ibfk_2', 'detailed_order', type_='foreignkey')
    op.drop_column('detailed_order', 'oid')
    op.drop_column('detailed_order', 'dprice')
    op.drop_column('detailed_order', 'orderid')
    op.drop_column('detailed_order', 'pid')
    op.drop_column('detailed_order', 'detailedoid')
    op.drop_column('detailed_order', 'number')
    op.add_column('official_user', sa.Column('imgURL', sa.Text(), nullable=True))
    op.add_column('official_user', sa.Column('isAdmin', mysql.TINYINT(), nullable=True))
    op.add_column('official_user', sa.Column('oDate', sa.DateTime(), nullable=True))
    op.add_column('official_user', sa.Column('oName', sa.String(length=500), nullable=True))
    op.add_column('official_user', sa.Column('oPassword', sa.String(length=500), nullable=True))
    op.add_column('official_user', sa.Column('official_userID', sa.Integer(), autoincrement=True, nullable=False))
    op.create_index(op.f('ix_official_user_official_userID'), 'official_user', ['official_userID'], unique=False)
    op.drop_index('ix_official_user_oid', table_name='official_user')
    op.drop_index('oname', table_name='official_user')
    op.create_unique_constraint(None, 'official_user', ['oName'])
    op.drop_column('official_user', 'oid')
    op.drop_column('official_user', 'isadmin')
    op.drop_column('official_user', 'odate')
    op.drop_column('official_user', 'imgurl')
    op.drop_column('official_user', 'oname')
    op.drop_column('official_user', 'opsd')
    op.add_column('product', sa.Column('iDate', sa.DateTime(), nullable=True))
    op.add_column('product', sa.Column('iName', sa.String(length=500), nullable=True))
    op.add_column('product', sa.Column('iPrice', mysql.DOUBLE(asdecimal=True), nullable=True))
    op.add_column('product', sa.Column('itemID', sa.Integer(), autoincrement=True, nullable=False))
    op.create_index(op.f('ix_product_itemID'), 'product', ['itemID'], unique=False)
    op.drop_index('ix_product_pid', table_name='product')
    op.drop_constraint('product_ibfk_2', 'product', type_='foreignkey')
    op.drop_constraint('product_ibfk_3', 'product', type_='foreignkey')
    op.drop_column('product', 'pdate')
    op.drop_column('product', 'oid')
    op.drop_column('product', 'pid')
    op.drop_column('product', 'pprice')
    op.drop_column('product', 'pname')
    op.drop_column('product', 'typeid')
    op.add_column('type', sa.Column('typeID', sa.Integer(), autoincrement=True, nullable=False))
    op.create_index(op.f('ix_type_typeID'), 'type', ['typeID'], unique=False)
    op.drop_index('ix_type_typeid', table_name='type')
    op.drop_column('type', 'typeid')
    op.add_column('user', sa.Column('imgURL', sa.Text(), nullable=True))
    op.add_column('user', sa.Column('tel', sa.String(length=500), nullable=True))
    op.add_column('user', sa.Column('uDate', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('uName', sa.String(length=500), nullable=True))
    op.add_column('user', sa.Column('uPassword', sa.String(length=500), nullable=True))
    op.add_column('user', sa.Column('userID', sa.Integer(), autoincrement=True, nullable=False))
    op.create_index(op.f('ix_user_userID'), 'user', ['userID'], unique=False)
    op.drop_index('ix_user_uid', table_name='user')
    op.drop_index('username', table_name='user')
    op.create_unique_constraint(None, 'user', ['uName'])
    op.drop_column('user', 'phone')
    op.drop_column('user', 'imgurl')
    op.drop_column('user', 'username')
    op.drop_column('user', 'userpsd')
    op.drop_column('user', 'date')
    op.drop_column('user', 'uid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('uid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.add_column('user', sa.Column('date', mysql.DATETIME(), nullable=True))
    op.add_column('user', sa.Column('userpsd', mysql.VARCHAR(length=500), nullable=True))
    op.add_column('user', sa.Column('username', mysql.VARCHAR(length=500), nullable=True))
    op.add_column('user', sa.Column('imgurl', mysql.TEXT(), nullable=True))
    op.add_column('user', sa.Column('phone', mysql.VARCHAR(length=500), nullable=True))
    op.drop_constraint(None, 'user', type_='unique')
    op.create_index('username', 'user', ['username'], unique=True)
    op.create_index('ix_user_uid', 'user', ['uid'], unique=False)
    op.drop_index(op.f('ix_user_userID'), table_name='user')
    op.drop_column('user', 'userID')
    op.drop_column('user', 'uPassword')
    op.drop_column('user', 'uName')
    op.drop_column('user', 'uDate')
    op.drop_column('user', 'tel')
    op.drop_column('user', 'imgURL')
    op.add_column('type', sa.Column('typeid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.create_index('ix_type_typeid', 'type', ['typeid'], unique=False)
    op.drop_index(op.f('ix_type_typeID'), table_name='type')
    op.drop_column('type', 'typeID')
    op.add_column('product', sa.Column('typeid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('product', sa.Column('pname', mysql.VARCHAR(length=500), nullable=True))
    op.add_column('product', sa.Column('pprice', mysql.DOUBLE(asdecimal=True), nullable=True))
    op.add_column('product', sa.Column('pid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.add_column('product', sa.Column('oid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('product', sa.Column('pdate', mysql.DATETIME(), nullable=True))
    op.create_foreign_key('product_ibfk_3', 'product', 'official_user', ['oid'], ['oid'])
    op.create_foreign_key('product_ibfk_2', 'product', 'type', ['typeid'], ['typeid'])
    op.create_index('ix_product_pid', 'product', ['pid'], unique=False)
    op.drop_index(op.f('ix_product_itemID'), table_name='product')
    op.drop_column('product', 'itemID')
    op.drop_column('product', 'iPrice')
    op.drop_column('product', 'iName')
    op.drop_column('product', 'iDate')
    op.add_column('official_user', sa.Column('opsd', mysql.VARCHAR(length=500), nullable=True))
    op.add_column('official_user', sa.Column('oname', mysql.VARCHAR(length=500), nullable=True))
    op.add_column('official_user', sa.Column('imgurl', mysql.TEXT(), nullable=True))
    op.add_column('official_user', sa.Column('odate', mysql.DATETIME(), nullable=True))
    op.add_column('official_user', sa.Column('isadmin', mysql.TINYINT(display_width=4), autoincrement=False, nullable=True))
    op.add_column('official_user', sa.Column('oid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'official_user', type_='unique')
    op.create_index('oname', 'official_user', ['oname'], unique=True)
    op.create_index('ix_official_user_oid', 'official_user', ['oid'], unique=False)
    op.drop_index(op.f('ix_official_user_official_userID'), table_name='official_user')
    op.drop_column('official_user', 'official_userID')
    op.drop_column('official_user', 'oPassword')
    op.drop_column('official_user', 'oName')
    op.drop_column('official_user', 'oDate')
    op.drop_column('official_user', 'isAdmin')
    op.drop_column('official_user', 'imgURL')
    op.add_column('detailed_order', sa.Column('number', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('detailed_order', sa.Column('detailedoid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.add_column('detailed_order', sa.Column('pid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('detailed_order', sa.Column('orderid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('detailed_order', sa.Column('dprice', mysql.DOUBLE(asdecimal=True), nullable=True))
    op.add_column('detailed_order', sa.Column('oid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('detailed_order_ibfk_2', 'detailed_order', 'order', ['orderid'], ['orderid'])
    op.create_foreign_key('detailed_order_ibfk_3', 'detailed_order', 'official_user', ['oid'], ['oid'])
    op.create_foreign_key('detailed_order_ibfk_4', 'detailed_order', 'product', ['pid'], ['pid'])
    op.create_index('ix_detailed_order_detailedoid', 'detailed_order', ['detailedoid'], unique=False)
    op.drop_index(op.f('ix_detailed_order_detailed_orderID'), table_name='detailed_order')
    op.drop_column('detailed_order', 'iNumber')
    op.drop_column('detailed_order', 'detailed_orderID')
    op.drop_column('detailed_order', 'dPrice')
    op.add_column('cart', sa.Column('uid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('cart', sa.Column('cprice', mysql.DOUBLE(asdecimal=True), nullable=True))
    op.add_column('cart', sa.Column('cnumber', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('cart', sa.Column('pid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('cart', sa.Column('cid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.create_foreign_key('cart_ibfk_1', 'cart', 'product', ['pid'], ['pid'])
    op.create_foreign_key('cart_ibfk_2', 'cart', 'user', ['uid'], ['uid'])
    op.create_index('ix_cart_cid', 'cart', ['cid'], unique=False)
    op.drop_index(op.f('ix_cart_cartID'), table_name='cart')
    op.drop_column('cart', 'cartID')
    op.drop_column('cart', 'cPrice')
    op.drop_column('cart', 'cNumber')
    op.create_table('order',
    sa.Column('orderid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('oprice', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('odate', mysql.DATETIME(), nullable=True),
    sa.Column('address', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('uid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['user.uid'], name='order_ibfk_1'),
    sa.PrimaryKeyConstraint('orderid'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_order_orderid', 'order', ['orderid'], unique=False)
    op.drop_index(op.f('ix_all_order_orderID'), table_name='all_order')
    op.drop_table('all_order')
    # ### end Alembic commands ###

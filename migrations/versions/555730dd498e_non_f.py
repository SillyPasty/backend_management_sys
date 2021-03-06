"""'non_f'

Revision ID: 555730dd498e
Revises: 
Create Date: 2020-06-30 17:11:51.577244

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '555730dd498e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('official_user',
    sa.Column('oid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('oname', sa.String(length=500), nullable=True),
    sa.Column('opsd', sa.String(length=500), nullable=True),
    sa.Column('odate', sa.DateTime(), nullable=True),
    sa.Column('isadmin', mysql.TINYINT(), nullable=True),
    sa.Column('imgurl', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('oid'),
    sa.UniqueConstraint('oname')
    )
    op.create_index(op.f('ix_official_user_oid'), 'official_user', ['oid'], unique=False)
    op.create_table('type',
    sa.Column('typeid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type1', sa.String(length=500), nullable=True),
    sa.Column('type2', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('typeid'),
    sa.UniqueConstraint('type1'),
    sa.UniqueConstraint('type2')
    )
    op.create_index(op.f('ix_type_typeid'), 'type', ['typeid'], unique=False)
    op.create_table('user',
    sa.Column('uid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=500), nullable=True),
    sa.Column('userpsd', sa.String(length=500), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('gender', sa.String(length=5), nullable=True),
    sa.Column('phone', sa.String(length=500), nullable=True),
    sa.Column('address', sa.String(length=500), nullable=True),
    sa.Column('imgurl', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_uid'), 'user', ['uid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_uid'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_type_typeid'), table_name='type')
    op.drop_table('type')
    op.drop_index(op.f('ix_official_user_oid'), table_name='official_user')
    op.drop_table('official_user')
    # ### end Alembic commands ###

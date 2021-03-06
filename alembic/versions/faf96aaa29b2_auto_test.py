"""auto test

Revision ID: faf96aaa29b2
Revises: f06c8e05bd7a
Create Date: 2017-03-29 15:57:12.626000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'faf96aaa29b2'
down_revision = 'f06c8e05bd7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TB')
    op.drop_table('ITEMSEND')
    op.drop_table('order')
    op.drop_table('LOG0221')
    op.drop_table('ALL0221')
    op.drop_table('TOTAL0221')
    op.drop_table('REPORT')
    op.add_column('user', sa.Column('nickname', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'nickname')
    op.create_table('REPORT',
    sa.Column('TID', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('TID'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('TOTAL0221',
    sa.Column('log_date', mysql.TIME(), nullable=True),
    sa.Column('tid', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('server', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('userip', mysql.VARCHAR(length=15), nullable=True),
    sa.Column('final_status', mysql.VARCHAR(length=15), nullable=True),
    sa.Column('bypassvalue', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('useragent', mysql.VARCHAR(length=500), nullable=True),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('ALL0221',
    sa.Column('TID', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('FINAL_STATUS', mysql.VARCHAR(length=15), nullable=True),
    sa.PrimaryKeyConstraint('TID'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('LOG0221',
    sa.Column('LOGDATE', mysql.TIME(), nullable=True),
    sa.Column('TID', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('SVR', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('BYPASSVALUE', mysql.VARCHAR(length=500), nullable=True),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('order',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('title', mysql.VARCHAR(length=45), nullable=True),
    sa.Column('status', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('ITEMSEND',
    sa.Column('TID', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('TID'),
    mysql_default_charset=u'tis620',
    mysql_engine=u'InnoDB'
    )
    op.create_table('TB',
    sa.Column('TID', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    # ### end Alembic commands ###

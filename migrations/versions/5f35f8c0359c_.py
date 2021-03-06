"""empty message

Revision ID: 5f35f8c0359c
Revises: d1e5403569bc
Create Date: 2016-06-06 18:11:08.416207

"""

# revision identifiers, used by Alembic.
revision = '5f35f8c0359c'
down_revision = 'd1e5403569bc'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('status', mysql.TINYINT(display_width=4), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'status')
    ### end Alembic commands ###

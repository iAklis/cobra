"""empty message

Revision ID: aef46ea30776
Revises: f5d5ac64ccfa
Create Date: 2016-06-07 16:30:21.149383

"""

# revision identifiers, used by Alembic.
revision = 'aef46ea30776'
down_revision = 'f5d5ac64ccfa'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('languages', 'language',
               existing_type=mysql.VARCHAR(length=32),
               type_=sa.String(length=11),
               existing_nullable=False)
    op.alter_column('projects', 'name',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=50),
               existing_nullable=True)
    op.alter_column('projects', 'repository',
               existing_type=mysql.VARCHAR(length=256),
               type_=sa.String(length=512),
               existing_nullable=True)
    op.alter_column('tasks', 'time_consume',
               existing_type=mysql.DATETIME(),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('tasks', 'time_end',
               existing_type=mysql.DATETIME(),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('tasks', 'time_start',
               existing_type=mysql.DATETIME(),
               type_=sa.Integer(),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'time_start',
               existing_type=sa.Integer(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
    op.alter_column('tasks', 'time_end',
               existing_type=sa.Integer(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
    op.alter_column('tasks', 'time_consume',
               existing_type=sa.Integer(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
    op.alter_column('projects', 'repository',
               existing_type=sa.String(length=512),
               type_=mysql.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('projects', 'name',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=True)
    op.alter_column('languages', 'language',
               existing_type=sa.String(length=11),
               type_=mysql.VARCHAR(length=32),
               existing_nullable=False)
    ### end Alembic commands ###

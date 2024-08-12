"""Initial migration

Revision ID: 25ee276e9fe7
Revises: 
Create Date: 2024-08-11 20:56:58.248375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25ee276e9fe7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('modelo', sa.String(length=100), nullable=False),
    sa.Column('categoria', sa.String(length=100), nullable=False),
    sa.Column('costo', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equipo')
    # ### end Alembic commands ###

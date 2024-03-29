"""add password

Revision ID: c62f395c5a28
Revises: 5c78443d06a0
Create Date: 2021-07-15 14:08:26.312480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c62f395c5a28'
down_revision = '5c78443d06a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###

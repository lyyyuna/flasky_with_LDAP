"""initial migration

Revision ID: 456ff69ea1bb
Revises: 3a723c39e739
Create Date: 2016-11-22 17:27:49.852703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '456ff69ea1bb'
down_revision = '3a723c39e739'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    ### end Alembic commands ###

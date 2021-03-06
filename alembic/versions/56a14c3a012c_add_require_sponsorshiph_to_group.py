"""Add sponsorship requirement option to group

Revision ID: 56a14c3a012c
Revises: 1f77e27629bd
Create Date: 2015-09-06 10:49:19.226136

"""

# revision identifiers, used by Alembic.
revision = '56a14c3a012c'
down_revision = '1f77e27629bd'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('group', sa.Column('requires_sponsorship', sa.Boolean(), default=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('group', 'requires_sponsorship')
    ### end Alembic commands ###

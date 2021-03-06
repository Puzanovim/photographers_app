"""add rejection field for order

Revision ID: 87e966967016
Revises: b5e5797f8d4b
Create Date: 2022-01-21 17:07:54.592070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87e966967016'
down_revision = 'b5e5797f8d4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('reason_for_rejection', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'reason_for_rejection')
    # ### end Alembic commands ###

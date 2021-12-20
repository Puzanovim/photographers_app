"""add order service

Revision ID: 8dde0f1d58b5
Revises: d608c6449570
Create Date: 2021-12-02 16:26:17.740003

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8dde0f1d58b5'
down_revision = 'd608c6449570'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('status', sa.Enum('new', 'in_progress', 'closed', 'canceled', name='orderstatus'), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('price', sa.String(), nullable=True),
    sa.Column('customer_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('performer_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['performer_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_status'), 'order', ['status'], unique=False)
    op.create_table('comment',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('author_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('order_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creation_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dates',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('start_datetime', sa.DateTime(timezone=True), nullable=False),
    sa.Column('end_datetime', sa.DateTime(timezone=True), nullable=False),
    sa.Column('order_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dates')
    op.drop_table('comment')
    op.drop_index(op.f('ix_order_status'), table_name='order')
    op.drop_table('order')
    # ### end Alembic commands ###
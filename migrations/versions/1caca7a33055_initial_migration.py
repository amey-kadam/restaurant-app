"""Initial migration

Revision ID: 1caca7a33055
Revises: 
Create Date: 2025-03-19 12:35:35.202702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1caca7a33055'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('logo_url', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('menu_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('is_available', sa.Boolean(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_number', sa.String(length=20), nullable=False),
    sa.Column('qr_code_url', sa.String(length=255), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('total_amount', sa.Float(), nullable=False),
    sa.Column('payment_status', sa.String(length=20), nullable=True),
    sa.Column('payment_id', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('table_id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.ForeignKeyConstraint(['table_id'], ['table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('special_instructions', sa.Text(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('menu_item_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['menu_item_id'], ['menu_item.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_item')
    op.drop_table('order')
    op.drop_table('table')
    op.drop_table('menu_item')
    op.drop_table('restaurant')
    # ### end Alembic commands ###

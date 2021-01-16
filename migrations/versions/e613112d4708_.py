"""empty message

Revision ID: e613112d4708
Revises: 3094a116c278
Create Date: 2021-01-16 15:23:49.426102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e613112d4708'
down_revision = '3094a116c278'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'age')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###

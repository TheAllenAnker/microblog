"""new fields in user model

Revision ID: 4df6c37b2461
Revises: 2da5a4002569
Create Date: 2018-05-24 11:49:03.057880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4df6c37b2461'
down_revision = '2da5a4002569'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###

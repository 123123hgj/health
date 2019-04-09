"""empty message

Revision ID: cee99f2e3104
Revises: b9b9c1d4e4d8
Create Date: 2019-04-08 17:07:41.212425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cee99f2e3104'
down_revision = 'b9b9c1d4e4d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('symptom', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('fk_symptom_admin_id_user', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_symptom_user_id_user'), 'user', ['user_id'], ['id'])
        batch_op.drop_column('admin_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('symptom', schema=None) as batch_op:
        batch_op.add_column(sa.Column('admin_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_symptom_user_id_user'), type_='foreignkey')
        batch_op.create_foreign_key('fk_symptom_admin_id_user', 'user', ['admin_id'], ['id'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###

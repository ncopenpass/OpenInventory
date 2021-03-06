"""initial version

Revision ID: 757dd9a0edba
Revises: 
Create Date: 2018-08-11 13:03:16.194238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '757dd9a0edba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('district',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('address', sa.String(length=256), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('created_ts', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_district_created_ts'), 'district', ['created_ts'], unique=False)
    op.create_index(op.f('ix_district_name'), 'district', ['name'], unique=False)
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('address', sa.String(length=256), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('created_ts', sa.DateTime(), nullable=True),
    sa.Column('district_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['district_id'], ['district.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_department_created_ts'), 'department', ['created_ts'], unique=False)
    op.create_index(op.f('ix_department_name'), 'department', ['name'], unique=False)
    op.create_table('truck',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('address', sa.String(length=256), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('created_ts', sa.DateTime(), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_truck_created_ts'), 'truck', ['created_ts'], unique=False)
    op.create_index(op.f('ix_truck_name'), 'truck', ['name'], unique=False)
    op.create_table('compartment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('created_ts', sa.DateTime(), nullable=True),
    sa.Column('truck_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['truck_id'], ['truck.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_compartment_created_ts'), 'compartment', ['created_ts'], unique=False)
    op.create_index(op.f('ix_compartment_name'), 'compartment', ['name'], unique=False)
    op.create_table('equipment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('created_ts', sa.DateTime(), nullable=True),
    sa.Column('compartment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['compartment_id'], ['compartment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_equipment_created_ts'), 'equipment', ['created_ts'], unique=False)
    op.create_index(op.f('ix_equipment_name'), 'equipment', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_equipment_name'), table_name='equipment')
    op.drop_index(op.f('ix_equipment_created_ts'), table_name='equipment')
    op.drop_table('equipment')
    op.drop_index(op.f('ix_compartment_name'), table_name='compartment')
    op.drop_index(op.f('ix_compartment_created_ts'), table_name='compartment')
    op.drop_table('compartment')
    op.drop_index(op.f('ix_truck_name'), table_name='truck')
    op.drop_index(op.f('ix_truck_created_ts'), table_name='truck')
    op.drop_table('truck')
    op.drop_index(op.f('ix_department_name'), table_name='department')
    op.drop_index(op.f('ix_department_created_ts'), table_name='department')
    op.drop_table('department')
    op.drop_index(op.f('ix_district_name'), table_name='district')
    op.drop_index(op.f('ix_district_created_ts'), table_name='district')
    op.drop_table('district')
    # ### end Alembic commands ###

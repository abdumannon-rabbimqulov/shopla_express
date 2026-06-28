"""Init couriers table

Revision ID: dc4f1aa983b4
Revises: 
Create Date: 2026-06-28 13:49:53.587552

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc4f1aa983b4'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('couriers',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('vehicle_type', sa.String(), nullable=False, server_default='SCOOTER'),
    sa.Column('passport_front_url', sa.String(), nullable=True),
    sa.Column('passport_back_url', sa.String(), nullable=True),
    sa.Column('texpassport_front_url', sa.String(), nullable=True),
    sa.Column('texpassport_back_url', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('pinfl', sa.String(), nullable=True),
    sa.Column('passport_number', sa.String(), nullable=True),
    sa.Column('car_plate_number', sa.String(), nullable=True),
    sa.Column('car_model', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_couriers_phone'), 'couriers', ['phone'], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_couriers_phone'), table_name='couriers')
    op.drop_table('couriers')

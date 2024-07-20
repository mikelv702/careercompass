



### Notes on Database Migrations


Creating a new revision
`alembic revision -m "Comment"`

Now we can update the file created in `/alembic/versions/<newversion>`

Here is an example of adding the quick tasks table that is attached to the user


```python

...

def upgrade():
    op.create_table('quicktasks',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('quicktasks')

```
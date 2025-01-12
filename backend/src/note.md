## Alembic tips:
> alembic init alembic

1. `Init Migration`
> alembic revision --autogenerate -m "Initial migration"

2. `Apply Migration latest version`
> alembic upgrade head

3. Keep repeating for update in future
4. Downgrade
> `alembic downgrade -1`
5. Current version
> `alembic current`
6. History migration
> `alembic history`

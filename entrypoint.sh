#!/bin/bash

# Migratsiyalarni amalga oshirish
echo "Alembic migratsiyalarini ishga tushirish..."
alembic upgrade head

# FastAPI ilovasini uvicorn orqali ko'tarish
echo "FastAPI serverni ishga tushirish..."
exec uvicorn main:app --host 0.0.0.0 --port 8000

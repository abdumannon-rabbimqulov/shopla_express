FROM python:3.13-slim

WORKDIR /app

# O'rnatish uchun kerakli tizim kutubxonalari
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Talablarni (requirements) o'rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Loyiha fayllarini nusxalash
COPY . .

# Uploads papkasini yaratish (rasmlar uchun)
RUN mkdir -p uploads

# Entrypoint scriptini ishga tushirish uchun ruxsat berish
RUN chmod +x entrypoint.sh

EXPOSE 8000

# Ilovani ishga tushirish
ENTRYPOINT ["./entrypoint.sh"]

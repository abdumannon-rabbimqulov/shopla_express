# Shopla va Express Delivery Integratsiyasi (Ishlash Logikasi)

Ushbu hujjat Shopla Marketplace'dan keladigan buyurtmalarni qabul qilish va kuryer orqali yetkazib berish jarayonini qisqa va tushunarli qilib tushuntiradi. Tizim **Event-driven (Hodisalarga asoslangan)** Webhook'lar orqali ishlaydi.

## 1. Zanjirning Boshlanishi (Order Ingestion)
* **Shopla harakati:** Xaridor Shopla'da naqd pulli (Cash on Delivery) buyurtma beradi.
* **Bizning tizim:** Shopla darhol bizga (Express API) yangi buyurtma haqida signal (Webhook) yuboradi. Tizimimiz buni qabul qilib, buyurtmaga `CREATED` (Yaratildi) statusini beradi.

## 2. Kuryerni Qidirish va Pulni Muzlatish (Match & Freeze)
* Tizim do'konga eng yaqin bo'lgan va liniyada (Online) turgan kuryerlarni qidirishni boshlaydi.
* **Filtr:** Kuryerning yonidagi naqd puli (`declared_cash`) buyurtma narxidan katta yoki teng bo'lishi shart.
* **Muzlatish:** Mos kuryer topilib, unga buyurtma biriktirilganda (`ASSIGNED`), uning yonidagi pulning buyurtmaga teng qismi vaqtincha "muzlatib" (`frozen_cash`) qo'yiladi. Bu orqali bitta kuryerga puli yetmaydigan bir nechta buyurtma berib yuborilishining oldi olinadi.

## 3. Kuryer Harakatlari va Shopla bilan Sinxronizatsiya
Kuryer o'z ilovasida qadam-baqadam tugmalarni bosib boradi. Har bir bosilgan tugma darhol Express tizimimiz orqali Shopla'ga signal (Webhook) bo'lib yetib boradi va mijoz o'z ilovasida jarayonni kuzatib turadi:

1. **Kuryer buyurtmani qabul qildi:** Status `ACCEPTED` ga aylanadi. Shopla'ga kuryerning ism-sharifi va raqami yuboriladi.
2. **Kuryer do'konga yetib bordi:** Status `ARRIVED_AT_STORE` ga o'zgaradi.
3. **Kuryer tovarlarni olib, yo'lga chiqdi:** Kuryer o'z yonidagi naqd pulni do'konga to'lab, tovarlarni oladi. Status `PICKED_UP` (Yo'lga chiqdi) bo'ladi.
4. **Kuryer mijozga yetkazib berdi:** Kuryer mijozdan tovar puli va dostavka haqini naqd ko'rinishida qaytarib oladi. Status `DELIVERED` (Yetkazildi) ga o'zgaradi.

## 4. Zanjirning Yopilishi (Billing va Hisob-kitob)
Status `DELIVERED` bo'lgandan so'ng, tizimda avtomatik hisob-kitob bo'ladi:
* Kuryerning vaqtincha muzlatilgan puli (`frozen_cash`) bekor qilinadi.
* Kuryerning yonidagi umumiy pulidan (`declared_cash`) do'konga to'lagan summasi yechib tashlanadi (chunki u o'z pulini mijozdan qaytarib oldi).
* Kuryerning tizimdagi virtual balansidan (Billing Balance) yetkazib berish xizmati uchun kompaniya komissiyasi ushlab qolinadi.
* **Jarayon to'liq va muvaffaqiyatli yakunlanadi.**

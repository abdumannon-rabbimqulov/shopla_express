# Shopla Express - Kuryer Ilovasi Loyihasi

## Loyiha Arxitekturasi (Project Architecture)

* **Backend API:** Python (FastAPI)

---

## Kuryerni Ro'yxatdan O'tkazish Ketma-ketligi (Registration Flow)

Kuryerni tizimdan ro'yxatdan o'tkazish jarayoni siz so'ragandek quyidagi bosqichlardan iborat bo'ladi:

### 1-bosqich: Telefon raqamini kiritish
* Kuryer ro'yxatdan o'tish (Register) oynasiga kiradi.
* O'zining faol telefon raqamini kiritadi (masalan, +998 90 123 45 67).
* Tizim bu raqam avval ro'yxatdan o'tgan yoki o'tmaganligini tekshiradi va davom etishga ruxsat beradi.

### 2-bosqich: Validatsiya va parol o'rnatish
* **Validatsiya (Tasdiqlash):** Telefon raqamiga SMS orqali bir martalik kod (OTP) keladi. Kuryer ushbu kodni ilovaga kiritib, telefon raqamini tasdiqlaydi.
* **Parol yaratish:** Raqam tasdiqlangach, kuryer o'z hisobiga kelajakda kirish uchun yangi parol o'rnatadi. Parolni takroran kiritib tasdiqlash so'raladi.

### 3-bosqich: Pasport ma'lumotlari va rasmlari (Verifikatsiya)
* Kuryer tizimda rasmiy ishlashi uchun shaxsini tasdiqlashi kerak bo'ladi.
* **Pasport (yoki ID karta) old qismi:** Ilova kuryerdan pasportning yuz tomoni (rasmi va asosiy ma'lumotlari bor qismi)ni rasmga olishni yoki galereyadan yuklashni so'raydi.
* **Pasport (yoki ID karta) orqa qismi:** Shu tarzda pasportning orqa qismini ham (yashash manzili kabi ma'lumotlar bilan) rasmga olib yuklaydi.
* Yuklangan hujjatlar xavfsiz tarzda serverga yuboriladi (fayl saqlash tizimiga joylanadi) va admin tomonidan tekshirilishi uchun jo'natiladi.

---

> **Eslatma:** Ushbu ro'yxatdan o'tish ma'lumotlari yig'ilgandan so'ng, kuryer akkaunti "kutilmoqda" (pending) holatiga o'tishi va tizim administratori hujjatlarni tekshirib tasdiqlaganidan so'nggina u to'liq faol holatga (active) o'tishi loyiha uchun maqsadga muvofiq bo'ladi.

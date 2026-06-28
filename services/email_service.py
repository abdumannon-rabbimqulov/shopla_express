import aiosmtplib
from email.message import EmailMessage
from core.config import settings
from datetime import datetime

async def send_mail(to: str, subject: str, html: str) -> dict:
    message = EmailMessage()
    message["From"] = settings.SMTP_FROM
    message["To"] = to
    message["Subject"] = subject
    message.set_content(html, subtype="html")

    try:
        await aiosmtplib.send(
            message,
            hostname=settings.SMTP_HOST,
            port=settings.SMTP_PORT,
            use_tls=settings.SMTP_SECURE,
            username=settings.SMTP_USER,
            password=settings.SMTP_PASSWORD,
        )
        print(f"📧 Email yuborildi: {to}")
        return {"success": True}
    except Exception as error:
        print(f"📧 Email yuborishda xatolik: {str(error)}")
        return {"success": False, "error": str(error)}

async def send_otp_email(email: str, code: str, expires_in_minutes: int = 3) -> dict:
    year = datetime.now().year
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 480px; margin: 0 auto; padding: 20px; background: #f5f5f5;">
  <div style="background: #fff; border-radius: 12px; padding: 32px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
    <div style="font-size: 28px; font-weight: 700; color: #1a1a1a; margin-bottom: 8px;">Shopla</div>
    <p style="color: #666; font-size: 15px; margin: 16px 0;">Tasdiqlash kodingiz:</p>
    <div style="background: #f0f7ff; border-radius: 8px; padding: 20px; margin: 20px 0;">
      <span style="font-size: 36px; font-weight: 700; letter-spacing: 8px; color: #2563eb;">{code}</span>
    </div>
    <p style="color: #999; font-size: 13px;">Kod {expires_in_minutes} daqiqa ichida amal qiladi.</p>
    <p style="color: #999; font-size: 13px;">Agar siz bu kodni so'ramagan bo'lsangiz, e'tiborsiz qoldiring.</p>
  </div>
  <p style="text-align: center; color: #bbb; font-size: 12px; margin-top: 16px;">© {year} Shopla</p>
</body>
</html>
"""
    return await send_mail(
        to=email,
        subject=f"{code} — Shopla tasdiqlash kodi",
        html=html_content
    )

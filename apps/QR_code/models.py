from django.db import models
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from apps.Basemodel.models import BaseModel


class QRCode(BaseModel):
    url = models.URLField(unique=True, verbose_name='URL')
    qr_code_image = models.ImageField(upload_to='qr_code_image/', blank=True, null=True, verbose_name='QR Code Image',
                                      help_text='Generated QR code image')

    def save(self, *args, **kwargs):
        if not self.qr_code_image:
            super().save(*args, **kwargs)
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(self.url)
            qr.make(fit=True)

            img = qr.make_image(fill_color="white", back_color="black").convert('RGB')

            with BytesIO() as buffer:
                img.save(buffer, format="PNG")
                self.qr_code_image.save(f'qr_code_{self.pk}.png', ContentFile(buffer.getvalue()), save=False)
                self.qr_code_image.save(f'qr_code_{self.pk}.png', ContentFile(buffer.getvalue()))

        else:
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'QR код'
        verbose_name_plural = 'QR код'

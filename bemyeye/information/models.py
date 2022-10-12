from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
# import gtts

class Information(models.Model):
    product_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    product_description = models.TextField(max_length=200)
    product_cost = models.IntegerField()
    manu_date = models.DateField()
    exp_date = models.DateField()
    product_image = models.FileField(upload_to = "products/", max_length = 250, null = True, default = None)

    qr_code = models.ImageField(upload_to = "qr_codes", blank = True)

    def __str__(self):
        return str(self.product_name)

    def save(self, *args, **kwargs):
        summary = "The name of the product is " + str(self.product_name) + ". The name of the company is " + str(self.company_name) + ". " + str(self.product_description) + " The cost of the product is " + str(self.product_cost) + ". The manufacturing date is " + str(self.manu_date) + ". The expiry date is " + str(self.exp_date)
        # print(summary)
        qrcode_img = qrcode.make(summary)
        canvas = Image.new('RGB', (1000, 1000), 'white')
        # draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.product_name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        # myobj = gtts.gTTS(text=summary, lang='en', slow=False)
        # myobj.save("static/speech.mp3")
        super().save(*args, **kwargs)

# Create your models here.

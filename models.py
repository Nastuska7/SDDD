from django.db import models


class Advertisement(models.Model):
    id = models.DecimalField("порядковый номер", decimal_places=0, max_digits=20)
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_length=10, decimal_places=2, max_digits=20) #decimal_places - количество чисел после точки
    action = models.BooleanField("торг", help_text='отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)#auto_now_add=True, чтобы дата сама автоматически выставлялась при добавлении этого поля
    created_up = models.DateTimeField(auto_now=True)# автоматически меняется(не добавляется)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
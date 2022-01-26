from django.db import models

# Create your models here.
class crowdmessage(models.Model):

    place_id = models.CharField('place_id',max_length=10,default='')
    then_time = models.DateTimeField('then_time',default='')
    crowd = models.DecimalField('crowd',max_digits=50,decimal_places=0,default='')
    class Meta:
        db_table = 'crowdmessage'

    def _str_(self):

        return '%s %s %s'%(self.place_id,self.thentime,self.crowd)

class syokudo_menu(models.Model):
    place_id = models.CharField('place_id',max_length=10,default='')
    place_name = models.CharField('place_name',max_length=50,default='')
    menu = models.CharField('menu',max_length=50,default='')
    price = models.DecimalField('price',max_digits=50,decimal_places=0,default='')
    kind = models.CharField('menu',max_length=50,default='')
    class Meta:
        db_table = 'syokudo_menu'

    def _str_(self):

        return '%s %s %s %s'%(self.place_id,self.syokudo_name,self.menu,self.price)
class place(models.Model):
    place_id = models.CharField('place_id',max_length=10,default='',primary_key=True,unique=True)
    place_name = models.CharField('place_name',max_length=50,default='')
    purpose = models.CharField('purpose',max_length=50,default='')
    using_time = models.CharField('using_time',max_length=50,default='')
    class Meta:
        db_table = 'place'

    def _str_(self):

        return '%s %s %s'%(self.place_id,self.place_name,self.purpose)

class pc_classroom(models.Model):
    place_id = models.ForeignKey(place,on_delete=models.CASCADE)
    place_name = models.CharField('place_name',max_length=50,default='')
    seating = models.CharField('seating',max_length=50,default='')
    class Meta:
        db_table = 'pc_classroom'

class rest_place(models.Model):
    place_id = models.ForeignKey(place,on_delete=models.CASCADE)
    place_name = models.CharField('place_name',max_length=50,default='')
    seating = models.CharField('seating',max_length=50,default='')
    class Meta:
        db_table = 'rest_place'

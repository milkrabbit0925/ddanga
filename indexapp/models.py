# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAdds(models.Model):
    id = models.IntegerField(primary_key=True)
    a_name = models.CharField(max_length=20, blank=True, null=True)
    a_address = models.CharField(max_length=40, blank=True, null=True)
    post_id = models.CharField(max_length=20, blank=True, null=True)
    # telephone = models.CharField(max_length=20, blank=True, null=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_adds'


class TBook(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=40, blank=True, null=True)
    author = models.CharField(max_length=40, blank=True, null=True)
    press = models.CharField(max_length=40, blank=True, null=True)
    pub_date = models.DateField(blank=True, null=True)
    edition = models.CharField(max_length=40, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    word_number = models.CharField(max_length=10, blank=True, null=True)
    page_number = models.CharField(max_length=10, blank=True, null=True)
    book_size = models.CharField(max_length=10, blank=True, null=True)
    paper = models.CharField(max_length=10, blank=True, null=True)
    packing = models.CharField(max_length=10, blank=True, null=True)
    book_class = models.ForeignKey('TClass', models.DO_NOTHING, db_column='book_class', blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    dd_price = models.FloatField(blank=True, null=True)
    editor_rec = models.CharField(max_length=2000, blank=True, null=True)
    about_content = models.CharField(max_length=2000, blank=True, null=True)
    about_author = models.CharField(max_length=1000, blank=True, null=True)
    catalog = models.CharField(max_length=2000, blank=True, null=True)
    media_comm = models.CharField(db_column='Media_comm', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    digest_image = models.CharField(max_length=2000, blank=True, null=True)
    illustration = models.CharField(max_length=2000, blank=True, null=True)
    series_name = models.CharField(max_length=40, blank=True, null=True)
    printing_date = models.DateField(blank=True, null=True)
    impression = models.CharField(max_length=10, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    shelves_date = models.DateField(blank=True, null=True)
    customer_score = models.FloatField(blank=True, null=True)
    book_status = models.IntegerField(blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book'


class TClass(models.Model):
    class_id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=20, blank=True, null=True)
    book_num = models.IntegerField(blank=True, null=True)
    class_pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_class'


class TOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    order_id = models.CharField(max_length=40, blank=True, null=True)
    cre_time = models.DateTimeField(blank=True, null=True)
    all_price = models.FloatField(blank=True, null=True)
    adss = models.ForeignKey(TAdds, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order'


class TOrderlterm(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    shop_bookid = models.ForeignKey(TBook, models.DO_NOTHING, db_column='shop_bookid', blank=True, null=True)
    shop_ordid = models.ForeignKey(TOrder, models.DO_NOTHING, db_column='shop_ordid', blank=True, null=True)
    shop_num = models.IntegerField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_orderlterm'


class TUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    username = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    c_time = models.DateTimeField(auto_now_add=True)
    has_check = models.BooleanField(default=False, verbose_name='是否确认')

    class Meta:
        managed = False
        db_table = 't_user'


class Check_user(models.Model):
    code = models.CharField(max_length=256,verbose_name='用户注册码')
    user = models.ForeignKey('TUser',on_delete=models.CASCADE,verbose_name='关联的用户')
    code_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'check_user'

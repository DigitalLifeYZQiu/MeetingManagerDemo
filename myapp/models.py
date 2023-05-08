from django.db import models
import datetime
# Create your models here.
class Conference(models.Model):#会议列表
    room_id=models.CharField(max_length=20)                #会议室名称
    allow_num=models.PositiveIntegerField(verbose_name="允许人数")    #剩余人数
    statu=models.BooleanField()         #会议状态
    meet_name=models.CharField(max_length=20)       #会议名
    operation=models.CharField(max_length=20)       #操作（预约）
    president=models.CharField(max_length=20)       #发起人
    start_time = models.DateTimeField(null=True)        #会议开始时间
    end_time = models.DateTimeField(null=True)          #会议结束时间
    sub_name = models.CharField(max_length=20)          #预约会议人的名字
    meet_kind = models.CharField(max_length=20)         #会议种类（文艺类、、、）
    class Meta:
        db_table='Conference'

#会议室表
class Manage_rooms(models.Model):#主要参数与会议列表的参数一致
        room_id=models.CharField(max_length=20)
        room_statu=models.BooleanField()   #会议室的状态（注意和会议的状态区分）
        allow_num=models.PositiveIntegerField(verbose_name="允许人数")
        open_starttime = models.DateTimeField(null=True)
        open_endtime = models.DateTimeField(null=True)
        class Meta:
            db_table = 'Manage_rooms'


#我的会议表
class My_list(models.Model):#此类里面的参数名称与会议名称一致
    room_id = models.CharField(max_length=20)
    allow_num = models.PositiveIntegerField(verbose_name="允许人数")
    statu = models.BooleanField()
    meet_name = models.CharField(max_length=20)
    operation = models.CharField(max_length=20)
    president = models.CharField(max_length=20)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    sub_name = models.CharField(max_length=20)
    meet_kind = models.CharField(max_length=20)

    class Meta:
        db_table='My_list'




#用户数据表
class User(models.Model):
    name=models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)#电话号码
    city=models.CharField(max_length=20)


    class Meta:
        db_table='User'



#用户参加过的会议
class Card(models.Model):
    room_id=models.CharField(max_length=20)
    meet_name=models.CharField(max_length=20)
    card_time=models.CharField(max_length=20)#打卡时间
    card_name=models.CharField(max_length=20)
    class Meta:
        db_table='Card'

#管理员
class admin(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    class Meta:
        db_table = 'admin'

#会议室内部情况
class Sub_room(models.Model):
    room_id=models.CharField(max_length=20)
    sub_name=models.CharField(max_length=20)
    sub_starttime=models.DateTimeField(null=True)
    sub_endtime = models.DateTimeField(null=True)

#通知
class Message(models.Model):
    message_time=models.DateTimeField(null=True)
    message_content=models.CharField(max_length=200)
    class Meta:
        db_table='Message'
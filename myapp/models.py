from django.db import models

# 事件表模型
class Event(models.Model):
    # 主键：事件唯一标识符
    event_id = models.AutoField(primary_key=True)
    
    # 子事件ID，用于构建树状结构
    child_event_id = models.IntegerField(null=True, blank=True)
    
    # 四象限分类
    QUADRANT_CHOICES = [
        ('IU', '重要紧急'),
        ('IN', '重要不紧急'),
        ('NU', '不重要紧急'),
        ('NN', '不重要不紧急'),
    ]
    quadrant = models.CharField(max_length=2, choices=QUADRANT_CHOICES)
    
    # 分类
    CATEGORY_CHOICES = [
        ('career', '事业'),
        ('hobby', '爱好'),
        ('life', '生活'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    
    # 事件标题
    title = models.CharField(max_length=200)
    
    # 事件描述或备注
    description = models.TextField(null=True, blank=True)
    
    # 截止日期
    deadline = models.DateField(null=True, blank=True)
    
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)
    
    # 更新时间
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

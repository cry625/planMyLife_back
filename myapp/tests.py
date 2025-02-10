from django.test import TestCase

# Create your tests here.
from myapp.models import Event
import random
from datetime import timedelta, datetime
# 示例数据生成函数
def generate_events():
    categories = ['career', 'hobby', 'life']
    quadrants = ['IU', 'INU', 'NU', 'NNU']
    titles = [
        "项目进度会议111", "健身计划", "家庭聚会", "阅读新书",
        "职业发展培训", "周末旅行", "学习新技能", "健康检查",
        "工作报告提交", "志愿者活动", "参加研讨会", "朋友聚餐",
        "写作计划", "整理房间", "社交活动", "参加课程",
        "制定预算", "参加音乐会", "看电影", "做饭",
        "参加运动会", "更新简历", "学习外语", "家庭游戏夜",
        "参加工作坊", "处理账单", "计划假期", "参加聚会",
        "清理邮箱", "参加网络研讨会", "制定职业目标", "学习编程",
        "参加摄影展", "做志愿者", "进行职业咨询", "参加社区活动",
        "制定饮食计划", "参加技能培训", "进行心理咨询", "参加读书会",
        "学习理财", "参加马拉松", "参加展览", "进行团队建设",
        "参加厨艺班", "进行家庭计划", "参加创意工作坊", "进行自我反思",
        "参加文化活动", "进行职业规划"
    ]

    events = []
    for _ in range(50):
        category = random.choice(categories)
        quadrant = random.choice(quadrants)
        title = random.choice(titles)
        description = f"{title} 的详细描述。"
        deadline = datetime.now() + timedelta(days=random.randint(1, 30))  # 随机截止日期

        event = Event(
            quadrant=quadrant,
            category=category,
            title=title,
            description=description,
            deadline=deadline.date(),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        events.append(event)

    return events

# 插入数据到数据库
def insert_events():
    events = generate_events()
    Event.objects.bulk_create(events)  # 批量插入
    print(f"成功插入 {len(events)} 条事件数据。")
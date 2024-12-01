# Generated by Django 5.1.3 on 2024-12-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('child_event_id', models.IntegerField(blank=True, null=True)),
                ('quadrant', models.CharField(choices=[('IU', '重要紧急'), ('IN', '重要不紧急'), ('NU', '不重要紧急'), ('NN', '不重要不紧急')], max_length=2)),
                ('category', models.CharField(choices=[('career', '事业'), ('hobby', '爱好'), ('life', '生活')], max_length=10)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
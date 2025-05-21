from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RainbowColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('hex_code', models.CharField(max_length=7)),
                ('order', models.IntegerField(unique=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
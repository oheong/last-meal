# Generated by Django 3.1.1 on 2020-09-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menuno', models.AutoField(db_column='menuNo', primary_key=True, serialize=False)),
                ('menuimgpath', models.ImageField(blank=True, db_column='menuImgPath', upload_to='menuimages/%Y/%m/')),
                ('menulist', models.CharField(db_column='menuList', max_length=255)),
                ('eattime', models.DateTimeField(db_column='eatTime')),
                ('tan', models.IntegerField(blank=True, db_column='tan', null=True)),
                ('dan', models.IntegerField(blank=True, db_column='dan', null=True)),
                ('ji', models.IntegerField(blank=True, db_column='ji', null=True)),
                ('dang', models.IntegerField(blank=True, db_column='dang', null=True)),
                ('na', models.IntegerField(blank=True, db_column='na', null=True)),
                ('cal', models.IntegerField(blank=True, db_column='cal', null=True)),
                ('col', models.IntegerField(blank=True, db_column='col', null=True)),
            ],
            options={
                'db_table': 'menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nutritional',
            fields=[
                ('nutritionalno', models.AutoField(db_column='nutritionalNo', primary_key=True, serialize=False)),
                ('nutritionalname', models.CharField(blank=True, db_column='nutritionalName', max_length=255, null=True)),
                ('tan', models.IntegerField(blank=True, null=True)),
                ('dan', models.IntegerField(blank=True, null=True)),
                ('ji', models.IntegerField(blank=True, null=True)),
                ('dang', models.IntegerField(blank=True, null=True)),
                ('na', models.IntegerField(blank=True, null=True)),
                ('cal', models.IntegerField(blank=True, null=True)),
                ('col', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'nutritional',
                'managed': False,
            },
        ),
    ]

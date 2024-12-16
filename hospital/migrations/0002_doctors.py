# Generated by Django 4.2.6 on 2024-03-12 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=100)),
                ('doc_spec', models.CharField(max_length=100)),
                ('doc_image', models.ImageField(upload_to='doctor')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.departments')),
            ],
        ),
    ]
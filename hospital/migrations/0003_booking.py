# Generated by Django 4.2.6 on 2024-03-13 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_doctors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('p_phone', models.CharField(max_length=10)),
                ('p_email', models.EmailField(max_length=254)),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctors')),
            ],
        ),
    ]

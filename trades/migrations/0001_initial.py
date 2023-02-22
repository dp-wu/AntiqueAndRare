# Generated by Django 4.1.7 on 2023-02-22 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('closed_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='pending', max_length=200)),
                ('offering_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offering_book', to='book.book')),
                ('requested_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_book', to='book.book')),
            ],
        ),
    ]

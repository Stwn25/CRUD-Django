# Generated by Django 5.1.3 on 2024-12-03 02:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waxsik_website', '0002_statuspemesanan_remove_pelanggan_layanan_dipesan'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailpemesanan',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pemesanan', to='waxsik_website.statuspemesanan'),
        ),
    ]

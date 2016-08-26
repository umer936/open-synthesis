# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 18:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openach', '0006_evidence_submit_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalystSourceTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_date', models.DateTimeField(verbose_name='date tagged')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openach.EvidenceSource')),
            ],
        ),
        migrations.CreateModel(
            name='EvidenceSourceTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=64)),
                ('tag_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='analystsourcetag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openach.EvidenceSourceTag'),
        ),
        migrations.AddField(
            model_name='analystsourcetag',
            name='tagger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

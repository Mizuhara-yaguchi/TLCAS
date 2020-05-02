# Generated by Django 3.0.5 on 2020-05-02 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PaperInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('paper_title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=300)),
                ('abstract', models.CharField(max_length=5000)),
                ('read_link', models.CharField(max_length=300)),
                ('pdf_link', models.CharField(max_length=300)),
                ('affiliations', models.CharField(max_length=300)),
                ('conference_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papers.ConferenceInfo')),
            ],
        ),
    ]

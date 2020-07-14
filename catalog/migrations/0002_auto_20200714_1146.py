# Generated by Django 3.0.8 on 2020-07-14 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(null=True, related_name='authors', to='catalog.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='shelf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Shelf'),
        ),
    ]

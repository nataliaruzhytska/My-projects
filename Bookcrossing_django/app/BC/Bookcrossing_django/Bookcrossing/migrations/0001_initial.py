# Generated by Django 3.0.1 on 2020-01-28 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Book name')),
                ('author', models.CharField(max_length=250, verbose_name='Author')),
                ('edition', models.CharField(blank=True, max_length=250, null=True, verbose_name='Edition')),
                ('year_ed', models.IntegerField(blank=True, null=True)),
                ('translator', models.CharField(blank=True, max_length=250, null=True)),
                ('is_visible', models.BooleanField(default=True, verbose_name='is_visible')),
            ],
            options={
                'ordering': ['name', 'author'],
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Library name')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, verbose_name='First name')),
                ('last_name', models.CharField(max_length=250, verbose_name='Last name')),
                ('email', models.CharField(blank=True, db_index=True, max_length=250, null=True)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['first_name', 'last_name'], name='Bookcrossin_first_n_be55ab_idx'),
        ),
        migrations.AddField(
            model_name='library',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bookcrossing.User'),
        ),
        migrations.AddField(
            model_name='book',
            name='lib_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Bookcrossing.Library'),
        ),
        migrations.AddField(
            model_name='book',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bookcrossing.User'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['name', 'author'], name='Bookcrossin_name_abfb44_idx'),
        ),
    ]
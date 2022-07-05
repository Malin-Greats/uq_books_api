# Generated by Django 4.0.4 on 2022-05-27 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BindingOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coil_bound', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('hard_cover', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('paper_back', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('saddle_stitch', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('linen_wrap', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A4', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('A5', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoverFinish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glossy', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('matte', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InteriorColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('black_white_prem', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('black_white_stan', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('color_prem', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('color_stan', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('under50', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('under100', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('under200', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('under300', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('under400', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaperType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cream', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('white', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('coated', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
            ],
        ),
    ]

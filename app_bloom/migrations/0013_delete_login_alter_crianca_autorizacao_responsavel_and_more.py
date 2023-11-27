# Generated by Django 4.2 on 2023-11-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bloom', '0012_alter_crianca_data_nascimento'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.AlterField(
            model_name='crianca',
            name='autorizacao_responsavel',
            field=models.FileField(upload_to='autorizacoes/'),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='data_nascimento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='historico_medico',
            field=models.FileField(upload_to='historicos/'),
        ),
    ]

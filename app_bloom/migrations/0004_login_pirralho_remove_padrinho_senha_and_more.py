# Generated by Django 4.2 on 2023-11-27 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bloom', '0003_remove_crianca_idade_crianca_autorizacao_responsavel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pirralho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.CharField(max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='padrinho',
            name='senha',
        ),
        migrations.AlterField(
            model_name='crianca',
            name='autorizacao_responsavel',
            field=models.FileField(upload_to='autorizacoes/'),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='data_nascimento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='endereco',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='genero',
            field=models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outro', 'Outro')], max_length=10),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='historico_medico',
            field=models.FileField(upload_to='historicos/'),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='rg',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='padrinho',
            name='cpf',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='padrinho',
            name='rg',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='padrinho',
            name='telefone',
            field=models.CharField(max_length=12),
        ),
    ]

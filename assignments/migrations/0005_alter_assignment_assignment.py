# Generated by Django 4.2.1 on 2023-05-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0004_remove_event_name_alter_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assignment',
            field=models.CharField(choices=[('ML', 'Microphone Direito'), ('MR', 'Microphone Esquerdo'), ('IA', 'Indicador Auditório'), ('IE', 'Indicador Entrada'), ('SV', 'Som e Vídeo'), ('FC', 'Dirigente de Campo'), ('RW', 'Leitor de Sentinela'), ('MC', 'Presidente')], max_length=2),
        ),
    ]

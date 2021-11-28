# Generated by Django 3.2.7 on 2021-11-28 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='barraca',
            field=models.ForeignKey(db_column='fk_barraca_id', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='produto_barraca_fk', to='projeto.barraca'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='preco_unitario',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='unidade',
            field=models.CharField(default='kg', max_length=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProdutoBarraca',
        ),
    ]

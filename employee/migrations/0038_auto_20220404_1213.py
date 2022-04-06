# Generated by Django 3.2.6 on 2022-04-04 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0037_remove_emergency_tel_remove_employee_tel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='religion',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='ssnitnumber',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='tinnumber',
        ),
        migrations.AlterField(
            model_name='employee',
            name='region',
            field=models.CharField(choices=[('Ahafo', 'Ahafo'), ('Ashanti', 'Ashanti'), ('Bono East', 'Bono East'), ('Bono', 'Bono'), ('Central', 'Central'), ('Eastern', 'Eastern'), ('Greater Accra', 'Greater Accra'), ('North East', 'Northen East'), ('Northen', 'Northen'), ('Oti', 'Oti'), ('Savannah', 'Savannah'), ('Upper East', 'Upper East'), ('Upper West', 'Upper West'), ('Volta', 'Volta'), ('Western North', 'Western North'), ('Western', 'Western')], default='Greater Accra', help_text='what region of the country(India) are you from ?', max_length=20, null=True, verbose_name='Region'),
        ),
        migrations.DeleteModel(
            name='Nationality',
        ),
        migrations.DeleteModel(
            name='Religion',
        ),
    ]

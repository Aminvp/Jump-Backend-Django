from django.db import migrations, models


def move_info(apps, _):
    Person = apps.get_model('people', 'Person')
    for person in Person.objects.all():
        person.first_name, person.last_name = map(
            lambda x: x.split(':')[1],
            person.fullname.split(';')
        )
        person.birth_year, person.born_in, person.id_code = map(
            lambda x: x.split(':')[1],
            sorted(person.information.split(';'))
        )
        person.save()


def reverse_move_info(apps, _):
    Person = apps.get_model('people', 'Person')
    for person in Person.objects.all():
        person.fullname = (
            f'first_name:{person.first_name};'
            f'last_name:{person.last_name}'
        )
        person.information = (
            f'birth_year:{person.birth_year};'
            f'born_in:{person.born_in};'
            f'id_code:{person.id_code}'
        )
        person.save()


class Migration(migrations.Migration):
    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birth_year',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='born_in',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='id_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.RunPython(
            code=move_info,
            reverse_code=reverse_move_info
        ),
        migrations.RemoveField(
            model_name='person',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='person',
            name='information',
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_year',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='born_in',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='id_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]

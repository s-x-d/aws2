from django.db import migrations

def add_rainbow_colors(apps, schema_editor):
    RainbowColor = apps.get_model('core', 'RainbowColor')
    
    # Create the rainbow colors
    colors = [
        ('Red', '#FF0000', 1),
        ('Orange', '#FF7F00', 2),
        ('Yellow', '#FFFF00', 3),
        ('Green', '#00FF00', 4),
        ('Blue', '#0000FF', 5),
        ('Indigo', '#4B0082', 6),
        ('Violet', '#9400D3', 7),
    ]
    
    for name, hex_code, order in colors:
        RainbowColor.objects.create(name=name, hex_code=hex_code, order=order)

def remove_rainbow_colors(apps, schema_editor):
    RainbowColor = apps.get_model('core', 'RainbowColor')
    RainbowColor.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_rainbow_colors, remove_rainbow_colors),
    ]
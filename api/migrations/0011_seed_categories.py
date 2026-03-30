from django.db import migrations

def create_categories(apps, schema_editor):
    # We fetch the Category model from the historical state
    Category = apps.get_model('api', 'Category')
    
    # List of permanent categories you want
    permanent_categories = [
        "Electronics",
        "Fashion",
        "Home & Living",
        "Health & Beauty",
        "Food & Beverages",
        "Sports & Outdoors",
        "Automotive",
    ]

    for name in permanent_categories:
        Category.objects.get_or_create(name=name)

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'), # This must match your first migration filename
    ]

    operations = [
        migrations.RunPython(create_categories),
    ]
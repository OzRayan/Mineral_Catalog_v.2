import json
import os

from django.core.wsgi import get_wsgi_application


def populate_db():
    """Populates db database. This should be done outside of project files
    and only called once at first launch"""
    # Setting up django default environment so Django can find project files
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mineral_catalog.settings")
    get_wsgi_application()

    # Setting up json file local directory path with absolute path
    local_directory = os.path.dirname(os.path.abspath(__file__))
    json_file = os.path.join(local_directory, 'assets/json/minerals.json')

    from minerals.models import Mineral

    with open(json_file, encoding='utf8') as js:
        fields = json.load(js)
        for field in fields:
            Mineral(
                name=field.get('name', ''),
                image_filename=field.get('image filename', ''),
                image_caption=field.get('image caption', ''),
                group=field.get('group', ''),
                category=field.get('category', ''),
                formula=field.get('formula', ''),
                strunz_classification=field.get('strunz classification', ''),
                color=field.get('color', ''),
                crystal_system=field.get('crystal system', ''),
                unit_cell=field.get('unit cell', ''),
                crystal_symmetry=field.get('crystal symmetry', ''),
                cleavage=field.get('cleavage', ''),
                mohs_scale_hardness=field.get('mohs scale hardness', ''),
                luster=field.get('luster', ''),
                streak=field.get('streak', ''),
                diaphaneity=field.get('diaphaneity', ''),
                optical_properties=field.get('optical properties', ''),
                refractive_index=field.get('refractive index', ''),
                crystal_habit=field.get('crystal habit', ''),
                specific_gravity=field.get('specific gravity', ''),
            ).save()


if __name__ == "__main__":
    populate_db()

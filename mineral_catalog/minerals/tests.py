from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Mineral


class MineralViewsTests(TestCase):
    """Views test class"""
    def setUp(self):
        """setUp method
        - Prepares 2 minerals for testing"""
        self.mineral_1 = Mineral.objects.create(
            name="Abelsonite",
            image_filename="240px-Abelsonite_-_Green_River_Formation%2C_Uintah_County%2C_Utah%2C_USA.jpg",
            category="Organic",
            image_caption="Abelsonite from the Green River Formation, Uintah County, Utah, US",
            group="Organic Minerals",
            formula="C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
            strunz_classification="10.CA.20",
            color="Pink-purple, dark greyish purple, pale purplish red, reddish brown",
            crystal_system="Triclinic",
            crystal_symmetry="Space group: P1 or P1Point group: 1 or 1",
            cleavage="Probable on {111}",
            mohs_scale_hardness="2–3",
            luster="Adamantine, sub-metallic",
            streak="Pink",
            diaphaneity="Semitransparent",
            optical_properties="Biaxial"
        )
        self.mineral_2 = Mineral.objects.create(
            name="Abernathyite",
            image_filename="240px-Abernathyite%2C_Heinrichite-497484.jpg",
            category="Arsenate",
            image_caption="Pale yellow abernathyite crystals and green heinrichite crystals",
            group="Arsenates",
            formula="K(UO<sub>2</sub>)(AsO<sub>4</sub>)·<sub>3</sub>H<sub>2</sub>O",
            strunz_classification="08.EB.15",
            color="Yellow",
            crystal_system="Tetragonal",
            unit_cell="a = 7.176Å, c = 18.126ÅZ = 4",
            crystal_symmetry="H-M group: 4/m 2/m 2/mSpace group: P4/ncc",
            cleavage="Perfect on {001}",
            mohs_scale_hardness="2.5–3",
            luster="Sub-Vitreous, resinous, waxy, greasy",
            streak="Pale yellow",
            diaphaneity="Transparent",
            optical_properties="Uniaxial (-)",
            refractive_index="nω = 1.597 – 1.608nε = 1.570"
        )

    def test_mineral_detail_view(self):
        """Mineral detail test
        - tests status code
        - tests mineral id
        - tests template used"""
        resp = self.client.get(reverse('minerals:mineral_detail', kwargs={'pk': self.mineral_1.id}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral_1.id, resp.context['mineral']['id'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')

    def test_random_mineral_view(self):
        """Mineral random test
        - tests lenght of random minerals, correct = 1"""
        minerals = set()
        for _ in range(15):
            resp = self.client.get('/minerals/random/')
            minerals.add(resp.context.get('pk'))
        self.assertEqual(len(minerals), 1)

    def test_mineral_list_view(self):
        """Minerals list test
        - tests status code
        - tests if mineral_1 and mineral_2 is in list
        - tests template used
        - tests if response contains mineral_1 name field"""
        resp = self.client.get(reverse('minerals:mineral_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_1, resp.context['minerals'])
        self.assertIn(self.mineral_2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral_1.name)

    def test_mineral_by_group_view(self):
        """Mineral group test
        - tests status code
        - tests template used
        - tests if response contain the group of <Organic Minerals>"""
        resp = self.client.get(reverse('minerals:mineral_by_group', kwargs={'group': self.mineral_1.group}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/group_list.html')
        self.assertContains(resp, 'Organic Minerals')

    def test_mineral_by_color_view(self):
        """Mineral color test
        - tests status code
        - tests template used
        - tests if response contain the color of <Yellow>"""
        resp = self.client.get(reverse('minerals:mineral_by_color', kwargs={'color': self.mineral_2.color}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/color_list.html')
        self.assertContains(resp, 'Yellow')

    def test_mineral_by_crystal_system(self):
        """Mineral crystal system test
        - tests status code
        - tests template used
        - tests if response contain the crystal system  of <Tetragonal>"""
        resp = self.client.get(reverse('minerals:mineral_by_crystal',
                                       kwargs={'crystal': self.mineral_2.crystal_system}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/crystal_list.html')
        self.assertContains(resp, 'Tetragonal')

    def test_mineral_by_alphabet(self):
        """Mineral starts with alphabet test
        - tests status code
        - tests template used
        - tests is response contains mineral_1 and mineral_2 name"""
        resp = self.client.get(reverse('minerals:mineral_alpha',
                                       kwargs={'alpha': 'A'}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral_1.name)
        self.assertContains(resp, self.mineral_2.name)

    def test_search_mineral(self):
        """Mineral search test
        - tests status code"""
        resp = self.client.get('/minerals/search/?mySelect=category&?q=Organic')
        self.assertEqual(resp.status_code, 404)

    def test_index(self):
        """Mineral starts with A test for index view
        - tests status code
        - tests templated used
        - tests if response contains mineral_1 and mineral_2 name which starts with A"""
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
        self.assertContains(resp, self.mineral_1.name)
        self.assertContains(resp, self.mineral_2.name)

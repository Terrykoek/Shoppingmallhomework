from shops.models import Shop
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

import os


class ShopTests(TestCase):
    def setUp(self):

        cwd = os.getcwd() + "/shops"  # Get the current working directory (cwd)
        cover_image = SimpleUploadedFile('images.jpeg', content=open(
            cwd+'/images.jpeg', 'rb').read(), content_type='image/jpeg')
        self.shop = Shop(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00',
            description='Harry and the ...',
            published_year=2000,
            cover=cover_image
        )

        self.shop.save()

    def test_shop_list(self):
        self.assertEqual(f'{self.shop.title}', 'Harry Potter')
        self.assertEqual(f'{self.shop.author}', 'JK Rowling')
        self.assertEqual(f'{self.shop.price}', '25.00')
        self.assertEqual(f'{self.shop.description}', 'Harry and the ...')

    def test_shop_index_view(self):
        response = self.client.get(reverse('shops_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'shops/index.html')

    def test_shop_detail_view(self):
        response = self.client.get(self.shop.get_absolute_url())
        self.assertEqual(response.status_code, 200)

        response1 = self.client.get('/show/34455')
        self.assertEqual(response1.status_code, 404)

        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'shops/show.html')
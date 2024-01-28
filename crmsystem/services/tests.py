from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from services.models import ServicesModel


class ProductListViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = ServicesModel.objects.create(name="qwerty", price=225.21)
        cls.users = User.objects.create_user(username="Bob", password="qwerty")

    @classmethod
    def tearDownClass(cls):
        cls.product.delete()
        cls.users.delete()


    def test_product_list(self):
        response = self.client.post(reverse("product:list"),
                                    {
                                        "name": "apple",
                                        "description": "a good phone",
                                        "price": "143",
                                    }
                                    )

        self.assertTrue(response)

    def test_product_list_page(self):
        response = self.client.get(reverse("product:list"))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_page(self):
        response = self.client.get(
            reverse("product:detail", kwargs={"pk": self.product.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_authentication_user(self):

        pathh = self.client.post(reverse("crm:login"), username=self.users.username, password=self.users.password)
        self.assertEqual(pathh.status_code, 200)
        self.assertTrue(pathh)

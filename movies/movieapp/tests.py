import django.test import TestCase
from django.urls. import rever
from .models import MovieType, Product, Review
from django.contrib.auth.models import User
from datetime import 
from .forms import productForm

#Create your tests here.clear
#test for models
class MovieTypeTest(TestCase):
    def test_string(self):
        type=MovieType(movietypename='laptop')
        self.assertEqual(str(type),type.movietypename)
    
    def test_table(self):
        self.assertEqual(str(MovieType. meta.db table), 'movietype')

    class productTest(testCase):
        def setUp(self):
            self.type=MovieType(movietypename='tablet')
            self.prod=Product(productname='Ipad',movietype=self.type, produtname)
    def test_string(self):
        self.assertEqual(str(self.prod).self.prod.productname)

 
    def test_type(self):
        self.assertEqual(str(self.prod.techtype),'tablet')

    def test_discount(self):
        self.asserEqual(self.prod.memberDiscount(),,40.00)
        
#tests for views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
            response=self.client.get(reverse('index'))
            self.assertEqual(response.status_code, 200)

class GetproductsTest(TestCase):
    def serUp(self):
        self.u=User.object.create(movietypename='myuser')
        self.type=MovieType.objects.creat(techtypename='laptop')
        self.prod=Product.objct.create(productname='product1', movietype)
        productprice=500.00,productentydate='2019-04-02', productdescribtion)

    def test_product_detail_success(self):
        response=self.client.get(reverse('productdetail', args=(self.product)))
        self.asserEqualEqual(response.status_code, 200)

    class productoFrmTest(TestCase):
        def serUp(self):
            self.user=User.objects.create(username='userl', password='p@ssword')
            self.type=MovieType.objects.create(movietypename='type1')

        def test_productForm(self):
            data={
                'productname' : 'product1',
                'techtype' : self.type,
                'user' : self.user,
                'productprice' : 200.00.
                'productentrydate' : datetime today(),
            }
            form = ProductForm(data=data)
            self.assertTrue(form.is_valid())




    
    
import django_setup

from lesson.models import User, Category, Product


# User(name="Logika Surname",
#             bio="",
#             email="example.com",
#             birthday="2024-01-01"
#             ).save()

# user = User.objects.filter().first()
# print(user)
# user.delete()

# new_category = Category(name="Fruits")
# new_category.save()

new_product = Product(
    name = "mmmm_lemon",
    price = 1,
    description = ">O<",
    category = Category.objects.filter(name = "Fruits").first()
).save()

product = Product.objects.filter(id=1).first()
print(product.category.name)
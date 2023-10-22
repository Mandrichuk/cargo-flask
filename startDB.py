import sqlite3
from provider_class import Provider
from product_class import Product

def get_providers_products():
  with sqlite3.connect("Cargo.db") as connect:
      cursor = connect.cursor()

      cursor.execute("""
      SELECT * FROM Providers 
      """)
      providers = [Provider(item[0], item[1], item[2]) for item in cursor.fetchall()]

      cursor.execute("""
      SELECT * FROM Products 
      """)
      products = [Product(item[0], item[1], item[2], item[3]) for item in cursor.fetchall()]

      for provider in providers: 
          for product in products:
              if provider.id == product.provider_id:
                  provider.product_list.append(product)
      

      return [providers, products]
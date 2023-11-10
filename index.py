from flask import Flask, render_template, request, redirect, url_for
import sqlite3

from provider_class import Provider
from product_class import Product

from update_data import update_data
from startDB import get_providers_products


providers = get_providers_products()[0]
products = get_providers_products()[1]
update_data(providers, products)


app = Flask("gluhaya_riba")

@app.route("/")
def main():
    providers = get_providers_products()[0]
    return render_template("index.html", providers=providers)


@app.route("/provider/<id>")
def provider(id):
    current_provider = [provider for provider in providers if provider.id == int(id)][0]
    return render_template("info.html", provider=current_provider)


@app.route("/control")
def control():
    return render_template("control.html")


@app.route("/action")
def action():
    global providers
    global products


    todo = request.args.get("todo")
    item_type = request.args.get("item_type")


    with sqlite3.connect("Cargo.db") as connect:
        cursor = connect.cursor()


        if item_type == "product":
            if todo == "adding":
                
                is_in_list = False
                for product in products:
                    if product.name == request.args["prod"]:
                        is_in_list = True

                if not is_in_list:
                    cursor.execute("""
                    INSERT INTO Products (PROVIDER_ID, NAME, PRICE, IMAGE) VALUES (?, ?, ?, ?)
                    """, (request.args["prov"], request.args["prod"], request.args["price"], request.args["image"]))

            elif todo == "removing":
                cursor.execute(f"""
                DELETE FROM Products
                WHERE Name = "{request.args["prod"]}"
                """)

            update_data(providers, products)
            

        if item_type == "provider":
            if todo == "adding":
                
                is_in_list = False
                for product in products: 
                    if product.name == request.args["prod"]:
                        is_in_list = True

                if not is_in_list:
                    cursor.execute("""
                    INSERT INTO Providers (NAME, PHONE) VALUES (?, ?)
                    """, (request.args["prov"], request.args["phone"]))

            elif todo == "removing":
                cursor.execute('PRAGMA foreign_keys = ON;')

                cursor.execute(f"""
                DELETE FROM Providers
                WHERE Name = "{request.args["prov"]}";
                """)

            update_data(providers, products)

        return redirect(url_for('all'))


@app.route("/all")
def all():
    with sqlite3.connect("Cargo.db") as connect:
        cursor = connect.cursor()

        cursor.execute("""
        SELECT * FROM Products
        """)
        products = [Product(item[0], item[1], item[2], item[3], item[4]) for item in cursor.fetchall()]
        prices_list = [product.price for product in products]
        
        sorted_list = sorted(prices_list)
        from_lowest_list = [product for price in sorted_list for product in products if price == product.price]
        
        reversed_sorted_list = sorted(prices_list, reverse=True)
        from_highest_list = [product for price in reversed_sorted_list for product in products if price == product.price]


    return render_template("all_products.html", from_lowest_list=from_lowest_list, from_highest_list=from_highest_list)


@app.route("/pricerange")
def pricerange():
    return render_template("pricerange.html")


@app.route("/rangedproducts")
def rangedlist():
    global providers
    global products

    range_products = []

    min_price = int(request.args["min"])
    max_price = int(request.args["max"])
   
    with sqlite3.connect("Cargo.db") as connect:
        cursor = connect.cursor()

        cursor.execute("""
        SELECT * FROM Products
        """)
        products = [Product(item[0], item[1], item[2], item[3], item[4]) for item in cursor.fetchall()]

        for product in products:
            if product.price >= min_price and product.price <= max_price:
                range_products.append(product)

        
        print(product.name for product in range_products)

    return render_template("rangedproducts.html", range_products=range_products, min_price=min_price, max_price=max_price)




if __name__ == "__main__":
    app.run(debug=True)
# Inventory Management Syestem Using OOPS
from abc import ABC, abstractmethod
from datetime import date,datetime
import json

class Product(ABC):

    def __init__(self,product_id,price,name,quantity_in_stock):
        self._name = name
        self._price = price
        self._product_id = product_id
        self._quantity_in_stock = quantity_in_stock

    @abstractmethod # @abstractmethod is used to mark a method as required
    def restock(self,amount):
        pass

    @abstractmethod
    def sell(self,quantity):
        pass

    @abstractmethod
    def get_total_value(self,price):
        pass

    @abstractmethod
    def __str__(self):
        pass

  
class Electronics(Product):
    def __init__(self, product_id, price, name, quantity_in_stock, warranty_years, brand):
        
        # super keyword is used to access the methodes and properties from parent class
        super().__init__(product_id, price, name, quantity_in_stock)
        self.warranty_years = warranty_years
        self.brand = brand

    def restock(self, amount):
        self._quantity_in_stock += amount

    def sell(self, quantity):
        if quantity <= self._quantity_in_stock:
            self._quantity_in_stock -= quantity
        else:
            print("\nNot enough stock to sell.")

    def get_total_value(self):
        return self._price * self._quantity_in_stock

    def __str__(self):
        return f"Electronics: {self._name} (Brand: {self.brand}, Warranty: {self.warranty_years} years, Price: {self._price}, Stock: {self._quantity_in_stock})"

      
class Grocery(Product):
    def __init__(self, product_id, price, name, quantity_in_stock, expiry_date):
        super().__init__(product_id,price,name,quantity_in_stock)
        self.expiry_date = expiry_date
    
    def restock(self, amount):
        self._quantity_in_stock += amount

    def sell(self, quantity):
        if quantity <= self._quantity_in_stock:
            self._quantity_in_stock -= quantity
        else:
            print("Not enough stock to sell.")

    def get_total_value(self):
        return self._price * self._quantity_in_stock  

    def is_expired(self):
        return date.today() > self.expiry_date

    def __str__(self):
        return f"Grocery: {self._name} (Expires on: {self.expiry_date}, Price: {self._price}, Stock: {self._quantity_in_stock}, Expired: {self.is_expired()})"

class Clothing(Product):
    def __init__(self, product_id, price, name, quantity_in_stock, size, material):
        super().__init__(product_id, price, name, quantity_in_stock)
        self.size = size
        self.material = material

    def restock(self, amount):
        self._quantity_in_stock += amount

    def sell(self, quantity):
        if quantity <= self._quantity_in_stock:
            self._quantity_in_stock -= quantity
        else:
            print("Not enough stock to sell.")

    def get_total_value(self):
        return self._price * self._quantity_in_stock

    def __str__(self):
        return f"Clothing: {self._name} (Size: {self.size}, Material: {self.material}, Price: {self._price}, Stock: {self._quantity_in_stock})"

class Inventory():
    def __init__(self):
        self._products = {}
    def add_product(self,product):
        self._products[product._product_id] = product

    def remove_product(self, product_id):
        if product_id in self._products:
            del self._products[product_id]

    def search_by_name(self, name):
        return [p for p in self._products.values() if p._name.lower() == name.lower()]

    def search_by_type(self, product_type):
        return [p for p in self._products.values() if isinstance(p, product_type)]

    def list_all_products(self):
        for product in self._products.values():
            print(product)  

    def sell_product(self, product_id, quantity):
        product = self._products.get(product_id)
        if product:
            product.sell(quantity)

    def restock_product(self, product_id, quantity):
        product = self._products.get(product_id)
        if product:
            product.restock(quantity)

    def total_inventory_value(self):
        return sum(product.get_total_value() for product in self._products.values())

    def remove_expired_products(self):
        expired_ids = [pid for pid, product in self._products.items()
                       if isinstance(product, Grocery) and product.is_expired()]
        for pid in expired_ids:
            del self._products[pid]   


INVENTORY_FILE = 'inventory.json'


def save_inventory(inventory):

    data = []
    for product in inventory._products.values():
        item = product.__dict__.copy() # copy all its properties
        item["__class__"] = product.__class__.__name__ # svae the product with class name

        item["__class__"] = product.__class__.__name__
        if isinstance(product, Grocery):
            item["expiry_date"] = product.expiry_date.isoformat()
        data.append(item)

    with open(INVENTORY_FILE , 'w') as file:
        json.dump(data , file , indent = 3)      


def load_inventory(inventory, filename="inventory.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            for item in data:
                cls = item.pop("__class__")

                # Convert underscored keys to regular ones
                product_data = {
                    "product_id": item["_product_id"],
                    "price": item["_price"],
                    "name": item["_name"],
                    "quantity_in_stock": item["_quantity_in_stock"]
                }

                if cls == "Electronics":
                    product_data["warranty_years"] = item["warranty_years"]
                    product_data["brand"] = item["brand"]
                    p = Electronics(**product_data)

                elif cls == "Grocery":
                    product_data["expiry_date"] = datetime.fromisoformat(item["_expiry_date"]).date()
                    p = Grocery(**product_data)

                elif cls == "Clothing":
                    product_data["size"] = item["size"]
                    product_data["material"] = item["material"]
                    p = Clothing(**product_data)

                inventory.add_product(p)

    except FileNotFoundError:
        print("No saved inventory found.")


if __name__ == "__main__":
    inventory = Inventory()
    load_inventory(inventory)

    while True:
        print("\n--- Inventory Management Menu ---")
        print("1. Add Product")
        print("2. Sell Product")
        print("3. Search/View Products")
        print("4. Save Inventory")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print("\nChoose Product Type: 1) Electronics 2) Grocery 3) Clothing")
            p_type = input("Enter type number: ")
            pid = input("Product ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            stock = int(input("Quantity in stock: "))

            if p_type == "1":
                brand = input("Brand: ")
                warranty = int(input("Warranty (years): "))
                product = Electronics(pid, price, name, stock, warranty, brand)
            elif p_type == "2":
                expiry_str = input("Expiry date (YYYY-MM-DD): ")
                expiry = datetime.strptime(expiry_str, "%Y-%m-%d").date()
                product = Grocery(pid, price, name, stock, expiry)
            elif p_type == "3":
                size = input("Size: ")
                material = input("Material: ")
                product = Clothing(pid, price, name, stock, size, material)
            else:
                print("Invalid type.")
                continue
            
            inventory.add_product(product)
            save_inventory(inventory)
            print("\nProduct added Successfully ✅.")

        elif choice == "2":
            pid = input("Enter Product ID to sell: ")
            qty = int(input("Enter quantity to sell: "))
            inventory.sell_product(pid, qty)

        elif choice == "3":
            print("\n1) View All Products\n2) Search by Name\n3) Search by Type")
            opt = input("Enter choice: ")
            if opt == "1":
                inventory.list_all_products()
            elif opt == "2":
                name = input("Enter name to search: ")
                results = inventory.search_by_name(name)
                for p in results:
                    print(p)
            elif opt == "3":
                print("Enter type: Electronics, Grocery, Clothing")
                type = input().lower()
                if type == "electronics":
                    results = inventory.search_by_type(Electronics)
                elif type == "grocery":
                    results = inventory.search_by_type(Grocery)
                elif type == "clothing":
                    results = inventory.search_by_type(Clothing)
                else:
                    print("❌ Invalid type.")
                    continue
                for p in results:
                    print(p)

        elif choice == "4":
            save_inventory(inventory)
            print("Inventory saved. ✅")


        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option.")

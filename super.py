class SuperMarket:
    def __init__(self):
        self.products = {
            "milk": 30,
            "bread": 20,
            "rice": 60,
            "oil": 100
        }
        self.cart = {}

    def show_products(self):
        print("\n🛍️ Available Products:")
        for item, price in self.products.items():
            print(f"{item.title()} - ₹{price}")

    def take_order(self):
        while True:
            product = input("\nEnter the product name to buy (or type 'done' to finish): ").strip().lower()
            if product == "done":
                break
            if product not in self.products:
                print("❌ Product not found. Please try again.")
                continue
            try:
                quantity = int(input(f"How many {product} do you want? "))
                if product in self.cart:
                    self.cart[product] += quantity
                else:
                    self.cart[product] = quantity
            except ValueError:
                print("❌ Invalid quantity. Please enter a number.")

    def generate_bill(self):
        if not self.cart:
            print("\n🛒 No items in cart. Thank you for visiting!")
            return

        print("\n🧾 Your Bill:")
        total = 0
        for product, quantity in self.cart.items():
            price = self.products[product]
            item_total = price * quantity
            total += item_total
            print(f"{product.title()} x {quantity} = ₹{item_total}")

        gst = total * 0.18
        grand_total = total + gst
        print(f"\nSubtotal: ₹{total}")
        print(f"GST (18%): ₹{gst:.2f}")
        print(f"Total Amount to Pay: ₹{grand_total:.2f}")
        print("🙏 Thank you for shopping with us!")


# ----------- Running the Supermarket Program -----------
store = SuperMarket()
store.show_products()
store.take_order()
store.generate_bill()

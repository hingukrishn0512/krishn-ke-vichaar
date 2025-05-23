class Solution(object):

    def greet(self,name):
        print(f"hello {name} what would you like to have :")
    
    def customer(self,product):
        self.products = {"fruits" : 250 , "coffee" : 100 , "cakes" : 200 , "cold drinks" : 20 }
        self.selected_product = None
        if product in self.products:
             self.selected_product = product
             print(f'ok sir , i repeat your order is {product}')
        else:
            print("your order is not available")

    def billing(self):
        if self.selected_product:
            price = self.products[self.selected_product]
            print(f"your bill amount is {self.selected_product} is {price} ")
        else:
            print("No product selected. Please place your order first.")

solution = Solution()
solution.greet("Krishn")
solution.customer("fruits")
solution.billing()


   






 
            


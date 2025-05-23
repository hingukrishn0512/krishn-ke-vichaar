class Solution(object):
    def greet(self, name):
        print(f"Hello {name}, how much do you want to withdraw or deposi ?")

    def choice(self, choose,total):
        
        if choose == 1:
            amount = float(input("Enter the amount you want to withdraw: "))
            print(f"You have withdrawn ₹{amount}")
            print(f"total amount in your bank now {total-amount}")
        elif choose == 2:
            amount = float(input("Enter the amount you want to deposit: "))
            print(f"You have deposited ₹{amount}")
            print(f"total amount in your bank now {total+amount}")
        else:
            print("Invalid choice. Please press 1 for withdrawal or 2 for deposit.")


solution = Solution()
solution.greet('krishn')
solution.choice(2 , 32000)
    

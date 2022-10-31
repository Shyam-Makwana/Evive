from collections import Counter

class Menu(object):
    def __init__(self, quantity):
        self.quantity = list(map(int, quantity.split(",")))
        self.quantity_count = Counter(self.quantity)
        self.final_order = []
        self.order = {"Breakfast": ["Eggs", "Toast", "Coffee"],
                      "Lunch": ["Sandwich", "Chips", "Soda"],
                      "Dinner": ["Steak", "Potatoes", "Wine", "Cake"]}
        self.mealtype = {"Breakfast": 3, "Lunch": 2, "Dinner": 0}
        self.error_message = ""

    def is_main_side_valid(self):
        main = True if 1 in self.quantity_count else False
        side = True if 2 in self.quantity_count else False

        is_valid = main and side

        if not is_valid:
            self.error_message += "Unable to process: "

            if not main and not side:
                self.error_message += "Main is missing, side is missing"
            else:
                if not main:
                    self.error_message += "Main is missing"

                if not side:
                    self.error_message += "Side is missing" 
            return False
        return True

    def is_order_valid(self, type):
        
        if type=="Dinner" and self.quantity_count[4]==0:
            self.error_message += "Unable to process: Dessert is missing"
            return False

        not_valid=[]

        for order in range(1,4):
            if(self.mealtype[type]!=order):
                if(order in self.quantity_count and self.quantity_count[order]>1):
                    not_valid.append(order)
                    
        if len(not_valid):
            self.error_message += "Unable to process: "
            while len(not_valid):
                current = not_valid.pop(0)
                self.error_message += str(self.order[type][current-1]) + " cannot be ordered more than once"
                if len(not_valid):
                    self.error_message += " and "
            return False
        else:
            return True

    def prepare_order(self, type):
        order_list = []
        
        order_list.append((self.order[type][0],1))
        order_list.append((self.order[type][1], self.quantity_count[2]))
        if self.quantity_count[3]:
            order_list.append((self.order[type][2], self.quantity_count[3]))
            if type == "Dinner":
                order_list.append(("Water", 1))
                order_list.append(("Cake", self.quantity_count[4]))
        else:
            order_list.append(("Water", 1))

        final_order = []

        for ord_num in order_list:
            order = str(ord_num[0])
            if ord_num[1]!=1:
                order += "(" + str(ord_num[1]) + ")"
            final_order.append(order)

        self.final_order = ", ".join(final_order)
    
    def process_order(self, type):
        if self.is_main_side_valid() and self.is_order_valid(type):
            self.prepare_order(type)
            return self.final_order
        else:
            return self.error_message

class Breakfast(Menu):
    def __init__(self, meal, quantity):
        Menu.__init__(self, quantity)
        self.meal = meal
    
    def get_order(self):
        return self.process_order(self.meal)

class Lunch(Menu):
    def __init__(self, meal, quantity):
        Menu.__init__(self, quantity)
        self.meal = meal

    def get_order(self):
        return self.process_order(self.meal)

class Dinner(Menu):
    def __init__(self, meal, quantity):
        Menu.__init__(self, quantity)
        self.meal = meal

    def get_order(self):
        return self.process_order(self.meal)

class Valid_Input():
    def __init__(self, input_order):
        self.input_order = input_order
        self.meals = ["Breakfast", "Lunch", "Dinner"]
        self.item = ['1', '2', '3', '4']
    
    def check_input(self):
        input_order = self.input_order.split()

        if len(input_order) != 2:
            self.input_order = self.input_order + " 0"
            return True
        else:
            meal, quantity = input_order
        
        if meal in self.meals:
            commas_count = quantity.count(',')
            quantity = quantity.split(',')
            if len(quantity)-1 == commas_count:
                for q in quantity:
                    if q not in self.item or ((meal==self.meals[0] or meal == self.meals[1]) and q == '4'):
                        return False
                return True
            else:
                return False
        else:
            return False

#Main Function
if __name__ == "__main__":
    input_order = input("In: ")
    order = Valid_Input(input_order)

    if order.check_input():
        meal, quantity = order.input_order.split()
        if meal == "Breakfast":
            meal_object = Breakfast(meal, quantity)
        elif meal == "Lunch":
            meal_object = Lunch(meal, quantity)
        elif meal == "Dinner":
            meal_object = Dinner(meal, quantity)
        
        print(meal_object.get_order())
    else:
        print("Enter valid input")
    





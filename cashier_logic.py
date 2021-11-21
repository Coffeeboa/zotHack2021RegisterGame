#cashier logic
EASY = 0
MEDIUM = 1
HARD = 2

import random


class Customer:
    def __init__(self, due: int or float, given: int or float):
        self._due = due
        self._given = given
        self._correct_change = round((self._given - self._due) , 2)

    def due(self): 
        return self._due
    
    def given(self):
        return self._given

    def correct_change(self):
        return self._correct_change
    

def _generate_amount_due(max_amount: int, decimals: int) -> float:
        '''Generate an amount due'''
        return round(random.random() * max_amount, decimals)


def _generate_amount_given(due: float, max_amount: int, decimals: int ) -> int:
    add = round(random.random() * max_amount, decimals) + due
    return round(add, decimals)

class CustomerState:
    #TODO add levels and difficulty variability 

    def __init__(self, line_length: int, difficulty: int):
        self._customer_line = []
        # TODO finish generating a list of customers
        if difficulty == EASY:
            self._customer_line = self._easy_customers(line_length)
            self._timer = 120


        elif difficulty == MEDIUM:
            self._customer_line = self._medium_customers(line_length)
            self._timer = 90
        
        elif difficulty == HARD:
            self._customer_line = self._hard_customers(line_length)
            self._timer = 60
        

    
    def _easy_customers(self, line_length: int) -> list[Customer]:
        line = []
        for x in range(line_length):
            due = _generate_amount_due(20, 0)
            given = _generate_amount_given(due, 10, 0)
            customer = Customer(due, given)
            line.append(customer)
        return line

    def _medium_customers(self, line_length: int) -> list[Customer]:
        line = []
        for x in range(line_length):
            due = _generate_amount_due(50, 2)
            given = _generate_amount_given(due, 25, 2)
            customer = Customer(due, given)
            line.append(customer)
        return line
    
    def _hard_customers(self, line_length: int) -> list[Customer]:
        line = []
        for x in range(line_length):
            due = _generate_amount_due(50, 2)
            given = _generate_amount_given(due, 50, 2)
            customer = Customer(due, given)
            line.append(customer)
        return line


    def customers_leave(self):
        new_customer_line = []
        for x in range(len(self._customer_line)):
            if self._customer_line[x].satisfaction() > 0:
                new_customer_line.append(self._customer_line[x])
        self._customer_line = new_customer_line
    
    def timer(self):
        return self._timer
    
        
    def line(self):
        return self._customer_line

    def remove_first_in_line(self):
        self._customer_line = self._customer_line[1:]

    
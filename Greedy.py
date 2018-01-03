# Greedy algorithm practice
# python version : 3.6

class Mygreedy(object):
    def __init__(self, items, values, costs, max_cost):
        self.max_cost = max_cost
        self.items = items
        self.values = values
        self.costs = costs
        self.min_cost_list = min(self.costs)
    def run_by_value(self):
        print('Greedy run by value ...********')
        num = 0
        cost = 0
        total_value = 0
        sorted_values = sorted(self.values, reverse=True)
        while True:
            index = self.values.index(sorted_values[num])
            if (cost+self.costs[index]) <= self.max_cost:
                cost += self.costs[index]
                item = self.items[index]
                value = self.values[index]
                print('item:',item, ',value:',value, ',cost:',cost)
                total_value += value
            if (cost+self.min_cost_list) >= self.max_cost  or num > 7:
                break
            num += 1
            if num > 7:
                break
        print('total value:', total_value)
        print('total cost:', cost)

    def run_by_cost(self):
        print('Greedy run by cost ...********')
        num = 0
        cost = 0
        total_value = 0
        sorted_values = sorted(self.costs, reverse=False)
        while True:
            index = self.costs.index(sorted_values[num])
            if (cost+self.costs[index]) <= self.max_cost:
                cost += self.costs[index]
                item = self.items[index]
                value = self.values[index]
                print('item:',item, ',value:',value, ',cost:',cost)
                total_value += value
            if (cost+self.min_cost_list) >= self.max_cost:
                break
            num += 1
            if num > 7:
                break

        print('total value:', total_value)
        print('total cost:', cost)


# 野外求生
items = ['rope', 'knife', 'fire', 'stone', 'money', 'food', 'clothes', 'phone']
values = [70, 100, 90, 30, 10, 80, 50, 40]
w = [50, 90, 35, 80, 25, 40, 60, 30]
max_cost = 100 # all weight you can choose

mygreedy = Mygreedy(items, values, w, max_cost)
mygreedy.run_by_value()
mygreedy.run_by_cost()




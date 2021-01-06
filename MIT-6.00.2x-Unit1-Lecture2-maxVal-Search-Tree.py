# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:15:55 2020

MIT 6.00.2x Introduction to Computational Thinking and Data Science
UNIT 1
Lecture 2

Maybe try finding an up-to-date link of the relevant year/edition of the course
Old link - stopped working Jan 2021
https://learning.edx.org/course/course-v1:MITx+6.00.2x+3T2020/
@author: Atanas Kozarev - github.com/ultraasi-atanas
"""
# =============================================================================
# Video:
# Brute Force Algorithms Search Tree Max Val
# =============================================================================

class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories  # in this example the cost is equal to calories, but cost can be time, money etc

    def density(self):  # here we define a metric - we wish to maximize the value to weight ratio
        return self.getValue() / self.getCost()

    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'


def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
    Returns a tuple of the total value of a solution to the 0/1 knapsack
    problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0,())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()

        # Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

        # Explore better branch
        if withVal > withoutVal:
            result = (withVal, withToHave + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


def runMaxVal(foods, maxUnits, printItems = True):


def buildMenu(food,val,cal):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                         calories[i]))
    return menu

# setting up the available options for the knappsack
names = ['wine','beer','pizza','burger','fries','cola',
             'apple','donut','cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]

# for convenience we lump all of the options in one variable called Menu
menu = buildMenu(names,values,calories)

#
maxUnits = 500

# running the thing
val, taken = maxVal(menu, maxUnits)
print('Use search tree to allocate', maxUnits, 'calories')
print('Total value of items taken =', val)
for item in taken:
    print('     ' + item)


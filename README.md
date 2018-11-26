# OOP Fundamentals Assignment

## Objectives
* define classes that satisfy test requirements
* write a program to demonstrate the usage of 
objects defined by classes
* demonstrate encapsulation principles by implementing attributes and methods of a class

## Part 1

### 1a - Coin Class
In Coin.py, define a Coin class that models a typical coin with two faces – `heads`
and `tails`

#### Attributes
`face` - string. Represents the value of the coin that is "faceing" up.  It can only be `heads` or `tails`

#### Methods
* `__init__(self)` - constructor method. Randomly sets the `face` attribute on creation of the object
* `get_face(self)` - returns the value of the `face` attribute
* `flip(self)` - randomly sets the value of the `face` attribute to `heads` or `tails`



### 1b - Coin Class Usage
In the main section of Coin.py, using the Coin class, write a program that simulates 1000 flips of a coin, keeping track of the total count of *heads* flips and *tails* flips.
Output the total *heads count* and total *tails count*.  Do not print out the result of each flip, only the total counts.


## Part 2
### 2a - Fraction Class
Define a Fraction class that models a fraction object.

#### Attributes
* `numerator` - int.  The numerator of a fraction.
* `denominator` - int. The denominator of a fraction

#### Methods
* `__init__(self,numerator, denominator)` - constructor method. 
Initializes the numerator and denominator attributes based parameters.  Raises a `ValueError` if the incoming `denominator` parameter is 0.
* `get_numerator(self)` - returns the value of the `numerator` attribute
* `get_denominator(self)` - returns the value fo the `denominator` attribute
* `set_numerator(self, new_numerator)` - set the value of the numerator attribute to the `int` parameter `new_numerator`.
* `set_denominator(self, new_denominator)` - set the value of the denominator attribute to the `int` parameter `new_denominator`.  Raises
a `ValueError` if `new_denominator` is 0.
* `__str__(self)` - returns the fraction in string form.  i.e "1/2".
* `add(self, otherFraction)` - adds `otherFraction` (another `Fraction` object) to the current `Fraction`.  Reduces the lowest terms if necessary.
* `subtract(self, otherFraction)` - subtracts `otherFraction` (another `Fraction` object) from the current `Fraction`.  Reduces the lowest terms if necessary.
* `multiply(self, otherFraction)` - multiplies the current fraction by `otherFraction` (another `Fraction` object).  Reduces the lowest terms if necessary.
* `__reduce(self)` - private method.  Reduces the fraction to lowest terms.

##### Note
The `__str__()` method is a special type of method.  When implemented for a class, it returns a string representation of the class when on object is referenced in a string expression.  For example:

```python
fraction` = Fraction(1,2)
print(fraction1)
```
outputs:
```python
1/2
```

Without a `__str__()` method implemented in the `Fraction` class, the memory address of the `fraction1` would be printed.

### 2b - Fraction usage
Write a program in the main section of Fraction.py that gets 2 sets of numerator and denominator values from user input and creates 2 Fraction objects.
Output the result of adding, subtracting, and multiplying the two fractions.

**Sample Run**

```python
** Fraction 1 **
Enter the numerator: 1
Enter the denominator: 2

** Fraction 2 **
Enter the numerator: 1
Enter the denominator: 4

1/2 + 1/4 = 3/4
1/2 - 1/4 = 1/4
1/2 * 1/4 = 1/8

```


## Testing & Other Stuff
* In Pycharm --> Settings (preferences in Mac OS) --> Tools/Python Integrated Tools change the `default test runner` to `unittest`.
* You can run the `Test_ ... .py` files to test your code. 
* Include docstring comments for your class methods.
* Commit after implementing each class method.
* Push your code periodically to github to back up.  Be sure to do one final push at the end.




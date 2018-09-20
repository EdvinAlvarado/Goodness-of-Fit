# Goodness-of-Fit
gives the chi-squared goodness of fit for different probability distributions. The Poisson distribution has been completely verified. binomial is implemented but still kinda broken. Normal distribution has not been verified. 


## addtill5 function

This was very difficult to implement due to needing to change the list that the loop was using and also due to the way that python address variables. 

### Addressing Issue

```Python
lst = [1,2,3]
moddedlist = lst
```

Any changes to **moddedlist** would change **lst**.

To fix this the moddedist gets the items appended. 

```Python
for i in lst:
    moddedlist.append(i)
```

This problem can be fixed for float and integer variables with:

```Python
number = 2
x = 0
x+= number
```

### Looping issue

By looping n about times so enough iterations are done for each possible number needed to be added

```Python
for i in range(len(l)):
    for i in range(len(lst)):
        if (lst[i] < 5.) and (i == 0):
                    lst[i] += lst[i+1]
                    lst.pop(i+1)
                    break
```

By breaking the loop after items are joined, it goes to the master loop effectively restarting the range of the slave loop which prevented the index and breaking issues.

## Probability Distributions

With the use of functions and some switches the interchanging of probability distributions and their corresponding degrees of freedom is very easy to do.

## Miscellaneous

There's also combination function, gamma function, and chi-squared function for anyone interested. There's also an unrelated python file called *test-list.py* which purpose was to take excel multi-variable data and create a 3d graphic. Right now it can take a string of numbers and build the list. However, I want to simply give it a plain text file without needing to transpose it and adding each variable one by one. I did do another one (upload this one later) for one with three variables but the amount of variables it can manage are static. I want to get around and see if it is possible to fix that. Maybe with a lists inside a master list.
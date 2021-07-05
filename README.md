# Stock Analyses 2017 & 2018

## Overview of Project

The main purpose of this project is to analyze a dataset that contains the stock data of green energy, for this we have de databases of two years 2017 and 2018. And the object is to know the behavior of this stocks to understand the data and take the best decision of what to invest in based on this analysis.

![Stocks of Green Energy]( https://phantom-expansion.unidadeditorial.es/cc097f095f3b7f8a82890aca5aa91ea6/resize/660/f/webp/assets/multimedia/imagenes/2021/06/15/16237785324667.jpg)


## Analysis and Refactoring Code

##Stocks Analysis

As the main purpose of the project is to know what is the best decision to invest in this green energies the first we need to do is analyze the behavior of the stocks in our databases for each year, this can give us a approach of how the stocks are behaving. First we can see that 2017 was a great year for green energies because most of the stocks in the data have a positive return, this means that final stock value of the year increase with respect to the initial value so that the return value that most of this stocks is positive and in some cases more that 100%, on the other hand we can see that this behavior is not constant because of the returns of 2018 that seems too much different for most of the stocks that has a negative return, with exception of ENPH and RUN stocks.
Base on the previous results the decision will be between ENPH and RUN stocks, as the return value of this two it’s still difficult to make a decision because we don’t have more historical information that can tell us more abut the behavior through the time, but if I have to make a decision I’ll invest in RUN stocks because the value of the return increase for 2018 and probably this is a good sign regarding behavior of the others stocks.

![Comparing Stocks Results]( https://github.com/alesandelmoral/stocks-analysis/blob/main/CompringStocksResults.PNG)

 
## Refactoring Code

One important part of coding is to optimize our code, in this case we make a refractor to our beginning code. As we can se in the next image the execution time decrease with respect of the initial code, this means that our code is more efficient that the previous one, maybe we can’t notice to much the different of time of both macros but in a complex analysis that has an amount of data this different it could be noticed more easily. Here are some points that I can notice:

1.	What are the advantage and disadvantage of refactoring code?

Advantages:
One advantage that I see when you are refactoring code is that in complex and bigger dataset you can optimize all the process and that a good thing because as people say time is money and more in the data analysis industry. Other advantage that I see is that if that you need to know very well your code to make these kinds of refactoring changes to your code, that’s means that you Know each line of your code or others code.

Disadvantages:
Maybe one disadvantage of refactoring is that in some cases it can be tedious to think on how the computer can easily process the code and be more efficient with the task, as I see is not a trivial work to do, and maybe will take to much time to repair something that works well but takes more time to execute.



2.	How do these pros and cons apply to refactoring the original script?

It’s takes less time to execute the code and make the task that we want the macro does, that a good pro, but in the other hand I think we are using more computer memory that we need, because we are creating an arrays to store all our information for only printing it on cells of out worksheet and we don’t use this arrays for something else.

![Comparing Time execution code]( https://github.com/alesandelmoral/stocks-analysis/blob/main/ComparingTimeCodes.PNG)

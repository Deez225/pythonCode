Algorithm for getting astrological sign according to month and day.

I have used variable 'mois' to designate the month and 'jour' variable to designate the day.
The subtle thing here is the way the condition was to be posed for example how to pose the condition 
for:

Aries: The Ram
(Mar 21-Apr 19)

The best way IMHO(In My Humble Opinion) is to decomposed like this:

 
 
 21 March  to 31 March 
 |-----------|    
 
       
 1 April to 19 April
 
 |--------------------------|
 
 thus, to be Ram must be in the interval [21 March, 31 March] or [1 April, 19 April].
 
 From where the python code:
 
 if (mois == 3 and (jour >= 21 and jour <= 31)) or (mois == 4 and (jour >= 1 and jour <= 20)):
    |-----------------------------------------|     |----------------------------------------|

1-January
2-February
3-March
4-April
...
For more information https://en.wikipedia.org/wiki/Astrological_sign 

Thanks to my friend hackaton94 who submitted me his problem for checking between month. 
    
    
    


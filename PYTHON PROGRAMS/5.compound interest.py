def  compound_interest(principal,rate,time):

     #calculates compound interest
     Amount =principal *(pow(( 1+rate/100),time ))
     CI=Amount -principal
     print ("compound interest is ",CI)


#Driver code
compound_interest (10000,10.25,5)     
                               
                              

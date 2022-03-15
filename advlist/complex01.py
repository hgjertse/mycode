#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    #display list1[1] which should only display arista_eos
    print(list1[1])

    #create a list called list #2
    list2=["juniper"]

    #extend list1 by list 2 (combine both lists into a single list)
    list1.extend(list2)

    #display list 1, which now contains juniper
    print(list1)

    #create a list and call it list #3
    list3=["10.1.0.1","10.2.0.1","10.2.0.1"]

    #use the append opperation to append list #1 by list #3
    list1.append(list3)

#print list 1
    print(list1)
#print 5th item in list 1
    print(list1[4])
#print the first IP Address
    print(list1[4][0])


main()


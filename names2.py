#!/usr/bin/env python3

def main():

    folks= ["David", "Elena", "Emily", "Chad", "Haley", "Jim", "Jonathan", "Matt", "Mike"]
    coolfolks=  []
    coolfolks= [i for i in folks if  len(i) > 4]

    print(coolfolks)

if __name__=="__main__":
    main()

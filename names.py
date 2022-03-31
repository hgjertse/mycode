#!/usr/bin/env python3

def main():

    folks= ["David", "Elena", "Emily", "Chad", "Haley", "Jim", "Jonathan", "Matt", "Mike"]

    coolfolks= []

   # for i  in folks:
    #   if i !="Chad":
     #       coolfolks.append(i)

   # print(coolfolks)
    coolfolks=[i for i in folks if i != "Chad"]
    print(coolfolks)
if __name__=="__main__":
    main()

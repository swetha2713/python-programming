#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     04/02/2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
bikes = ['trek','redline','giant']
first_bike = bikes[0]
last_bike = bikes[-1]
for bike in bikes:
    print(bike)

bikes.append('1')
bikes.append('2')
bikes.append('3')

for bike in bikes:
    print(bike)
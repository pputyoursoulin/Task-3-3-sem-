import math

file = open('data.txt')

try:
    circle1 = list(map(float, file.readline().split()))

    if len(circle1) != 3:
         print('Error!!! The data in the file is incorrect!\n')
    else:
         CoordX1 = circle1[0]
         CoordY1 = circle1[1]
         Radius1 = circle1[2]

    circle2 = list(map(float, file.readline().split()))

    if len(circle2) != 3:
         print('Error!!! The data in the file is incorrect!\n')
    else:
         CoordX2 = circle2[0]
         CoordY2 = circle2[1]
         Radius2 = circle2[2]

    dist = math.sqrt((CoordX1-CoordX2)**2  + (CoordY1-CoordY2)**2)

    if dist < math.fabs(Radius1-Radius2):
        print('One circle is in another circle\n')
    else:
        if dist > (Radius1+Radius2):
            print('One circle lies outside the other\n')
        else:
            if dist == math.fabs(Radius1-Radius2):
                print('The circles touch from the inside\n')
            else:
                if dist == (Radius1+Radius2):
                    print('The circles touch from the outside\n')
                else:
                    print('The circles intersect at two points\n')
                    
except ValueError:
    print('Error!!! The data in the file is incorrect!\n')

file.close()

from clsEllipse import Ellipse

for count in range(0, 8):
    nums = input("What are the numbers? ")
    numsList = nums.split(", ")
    ellipse = Ellipse(int(numsList[0]), int(numsList[1]), int(numsList[2]), int(numsList[3]), int(numsList[4]), int(numsList[5]))
    origX, origY = ellipse.getCenter()
    print("%s, (%d, %d), %d" % ("Circle" if ellipse.isCircle() else "Ellipse", origX, origY, ellipse.getMajorAxis() if ellipse.isEllipse() else int(ellipse.getMajorAxis()/2)))

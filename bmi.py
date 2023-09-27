def showprogramname() :
    print(' ---- โปรแกรมคำนวณสูตร BMI ----')

def inputData( ) :
    weight = int( input('ป้อนนํ้าหนัก (กิโลกรัม) : ') )
    height = int( input('ป้อนส่วนสูง (เมตร) : ') )
    return weight, height, 

def BMI1( weight,height) :
    BMI = weight / (height**2)
    return BMI

def showBMI (BMI, weight, height) :
    print('นํ้าหนัก {} ส่วนสูง {} BMI = {}'.format(weight, height, "{:.2f}".format(BMI)))
    print('นํ้าหนัก', weight, 'ส่วนสูง', height, 'BMI =', "{:.2f}".format(BMI))
    print(f'นํ้าหนัก {weight} ส่วนสูง {height} BMI = {"{:.2f}".format(BMI)}')
    print('นํ้าหนัก ' + str(weight) + ' ส่วนสูง ' + str(height) + ' BMI = ' + str("{:.2f}".format(BMI)))
    


print('--------------------------------------')
showprogramname()
print('--------------------------------------')
weight, height = inputData()
print('--------------------------------------')
BMI = BMI1(weight, height)
print('--------------------------------------')
showBMI (BMI,weight,height)
print('--------------------------------------')
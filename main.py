import centroid
import math

soal = int(input('1.sheckl khas 2.shecl marof'))
k = int(input(' : لطفا تعداد اجزا شکل را مشخص کنید'))


i = 1

x1 = 0
y1 = 0
a1 = 0

while i <= k :
    i += 1
    ajza = int(input(' :لطفا نوع شکل  را مشخص کنید 1.مستطیل یا 2.مثلث یا 3.ربع دایره یا 4.نیم دایره یا 5. نیم بیضی یا 6. ربع بیضی یا 7.سهموی یا 8. نیم سهوی یا 9. اسپاندرول'))
    noe = int(input('1.to por ya 2.to khali'))
    
    if ajza == 1:
        l = int(input('enter l: '))
        h = int(input('enter h: '))
        x,y = centroid.mostatil(l, h)
        a = l * h 
        if noe == 1:
            x1 += a * x
            y1 += a * y
            a1 += a
        elif noe == 2:
            x1 -= a * x
            y1 -= a * y
            a1 -= a
    elif ajza == 2:
        h = int(input('enter h: '))
        b = int(input('enter qaedeh: '))
        x,y = centroid.mosalas(h)
        a = b * h /2
        if noe == 1:
            x1 += a * x
            y1 += a * y
            a1 += a
        elif noe == 2:
            x1 -= a * x
            y1 -= a * y
            a1 -= a
    elif ajza == 3:
        r = int(input('enter r: '))
        a = math.pi * math.pow(r, 2) / 4
        x,y = centroid.robdaire(r)
        if noe == 1:
            x1 += a * x
            y1 += a * y
            a1 += a
        elif noe == 2:
            x1 -= a * x
            y1 -= a * y
            a1 -= a
    elif ajza == 4:
        r = int(input('enter r :'))
        a = math.pi * math.pow(r, 2) / 2
        x,y = centroid.nimdaiere(r)
        if noe == 1:
            x1 += a * x
            y1 += a * y
            a1 += a
        elif noe == 2:
            x1 -= a * x
            y1 -= a * y
            a1 -= a
    elif ajza == 5 :
        s = int(input('enter a: '))
        b = int(input('enter b: '))
        a = math.pi * b * s / 2
        x,y = centroid.nimbeiezi(s, b)
        if noe == 1:
            x1 += a * x
            y1 += a * y
            a1 += a
        elif noe == 2:
            x1 -= a * x
            y1 -= a * y
            a1 -= a
    elif ajza == 6 :
        s = int(input('enter a: '))
        b = int(input('enter b: '))
        a = math.pi * b * s / 4
        x,y = centroid.robbeizi(s, b)
        if noe == 1:
            x1 += a * x
            y1 += a * y
            a1 += a
        elif noe == 2:
            x1 -= a * x
            y1 -= a * y
            a1 -= a
    elif ajza == 7 :
        s = int(input('enter a:'))
        b = int(input('enter b: '))
        a = 2 * s * b /3 
        x,y = centroid.sahmavi(s, h)
        if noe == 1:
            x1 += a * x
            y1 += a * y
            a1 += a
        elif noe == 2:
            x1 -= a * x
            y1 -= a * y
            a1 -= a
    elif ajza == 8 :
        n = int(input('enter n of pow:'))
        h = int(input('enter h: '))
        a = int(input('enter a: '))
        x,y = centroid.spandrol(a, h, n)
        if noe == 1:
            x1 += a * x
            y1 += a * y
            a1 += a
        elif noe == 2:
            x1 -= a * x
            y1 -= a * y
            a1 -= a


x_c = x1/a1
y_c = y1/a1

print(f'x is : {x_c}')
print(f'y is : {y_c}')
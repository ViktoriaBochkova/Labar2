"""
height=2
weight=120
step_number=1000
active_time=60
"""
height=float(input("Введите ваш рост"))
weight=float(input("Введите ваш вес"))
step_number=float(input("Введите кол-во шагов"))
active_time=float(input("Введите время активности"))

step=height/4+0.37
dist=step*step_number

speed=dist/active_time

calor=0.035*weight+(speed**2/height)*0.029*weight
print('пройденная дистанция',dist,'сожженных калории',calor)
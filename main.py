height=2
weight=120
step_number=1000
active_time=60


step=height/4+0.37
dist=step*step_number

speed=dist/active_time

calor=0.035*weight+(speed**2/height)*0.029*weight
print('пройденная дистанция',dist,'сожженных калории',calor)
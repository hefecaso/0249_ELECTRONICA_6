def contador():
  numero = 0
  while True:
    numero += 1
    yield numero

cuenta = contador()
for i in range(1000):
   print(f"Azimut {next(cuenta)}° | Elevación {next(cuenta)}°")
   time.sleep(2)

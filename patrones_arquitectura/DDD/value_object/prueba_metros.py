from DDD.value_object.metros import *


metros_casa = Metros(100)
metros_caminar = Metros(50)
metros_patio = Metros(100)



print(metros_casa.distancia_en_metros)

print(metros_casa.distancia_en_metros == metros_caminar.distancia_en_metros)

print(metros_patio.distancia_en_metros == metros_casa.distancia_en_metros)

print("{0} yardas".format(metros_casa.en_yardas().distancia_en_yardas))

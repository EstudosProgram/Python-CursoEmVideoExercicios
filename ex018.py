import math

angulo = int(input('Digite o ângulo: '))
print('O ângulo de {} graus tem o seno de: {:.2f} \nO ângulo de {} graus tem o cosseno de: {:.2f} \nO ângulo de {} graus tem a tangente de: {:.2f}'.format(angulo, math.sin(math.radians(angulo)), angulo, math.cos(math.radians(angulo)), angulo, math.tan(math.radians(angulo))))
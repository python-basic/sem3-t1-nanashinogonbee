initial = int(''.join(c for c in input('init: ') if c.isdigit()))
step = int(''.join(c for c in input('step: ') if c.isdigit()))
print(', '.join(str(initial + step * i) for i in range(int(input('qty: ')))))

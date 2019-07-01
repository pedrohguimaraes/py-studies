for i in range(5):
    print(i)

impostos = ['MEI', 'Simples']
for imposto in impostos:
    if imposto.startswith("S"):
        continue
print(imposto)

print("Antes do loop")
for i in range(10):
    print(f"Loop {i}")
    # Simulação de código que pode estar travando
    if i == 5:
        break
print("Depois do loop")

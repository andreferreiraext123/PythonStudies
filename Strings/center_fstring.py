# Operations of centering, rjust and ljust using the f-string

string = 'André'


print(f"{'string':.>20}") # Equivalent as rjust
print(f"{'string':.<20}") # Equivalent as ljust
print(f"{'string':.^20}") # Equivalent as center
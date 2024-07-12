
vlan = input("Ingrese el número de VLAN: ")


try:
    vlan = int(vlan)
except ValueError:
    print("Por favor, ingrese un número válido.")
    exit()


rango_normal = range(1, 1006)
rango_extendido = range(1006, 4096)

if vlan in rango_normal:
    print(f"La VLAN {vlan} corresponde al rango normal.")
elif vlan in rango_extendido:
    print(f"La VLAN {vlan} corresponde al rango extendido.")
else:
    print("Número de VLAN fuera del rango válido (1-4095).")

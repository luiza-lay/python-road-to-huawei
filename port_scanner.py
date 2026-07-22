attackers = {
    "192.168.1.1": [22, 80, 443],
    "10.0.0.1": [23, 445],
    "8.8.8.8": [53],
    "1.1.1.1": [25, 135]
}

print("=== Список атакующих IP ===")
print(attackers)

ip = input("\nВведите IP для проверки: ")

if ip in attackers:
    print(f" IP {ip} в чёрном списке!")
    print(f"Атакующие порты: {attackers[ip]}")
else:
    print(f" IP {ip} безопасен")


port_check = input("\nХотите проверить порт? (да/нет): ")

if port_check.lower() == "да":
    port = int(input("Введите порт: "))
    if ip in attackers:
        if port in attackers[ip]:
            print(f" {ip}:{port} — АТАКА ОБНАРУЖЕНА!")
        else:
            print(f" {ip}:{port} — порт безопасен")
    else:
        print(f"IP {ip} не найден в базе атакующих")


else:
    print("Проверка порта отменена")














    
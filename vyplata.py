hours_worked = int(input("Zadej počet odpracovaných hodin: "))
hourly_rate = float(input("Zadej hodinovou sazbu (Kč): "))

gross_pay = hours_worked * hourly_rate

tax = gross_pay * 0.15
net_pay = gross_pay - tax

print()
print(f"{'Odpracované hodiny:':<25}{hours_worked:>10}")
print(f"{'Hodinová sazba:':<25}{hourly_rate:>10.2f}")
print(f"{'Hrubý plat:':<25}{gross_pay:>10.2f}")
print(f"{'Daň (15%):':<25}{tax:>10.2f}")
print(f"{'Čistý plat:':<25}{net_pay:>10.2f}")
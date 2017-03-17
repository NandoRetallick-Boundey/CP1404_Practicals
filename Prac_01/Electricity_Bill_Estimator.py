
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

price_per_kWh = int(input("Which tariff? 11 or 31: "))

daily_use_per_kWh = float(input("Enter dailyuse in kWh: "))

billing_cycle = int(input("Enter number of billing days: "))

if price_per_kWh == 11:
    estimated_bill = ((TARIFF_11 * daily_use_per_kWh) * billing_cycle)
else:
    estimated_bill = ((TARIFF_31 * daily_use_per_kWh) * billing_cycle)

print("Estimated bill: ${:.2f}".format(estimated_bill))

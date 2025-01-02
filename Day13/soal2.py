import csv, os

fileName = "inventaris_barang.csv"

if not os.path.exists(fileName):
    print(f"File {fileName} tidak ditemukan.")
    inventory = []
else:
    inventory = []
    with open(fileName, mode="r") as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            if len(row) == 2:
                barang, jumlah = row
                if jumlah.isdigit():
                    inventory.append({"barang": barang, "jumlah": int(jumlah)})
                else:
                    print(f"Format data salah pada baris: {row}")

updates = [
    {"barang": "Buku", "perubahan": 5}, # Menambah
    {"barang": "Pensil", "perubahan": -5} # mengurang
]

for update in updates:
    found = False
    for item in inventory:
        if item["barang"].lower() == update["barang"].lower():
            item["jumlah"] += update["perubahan"]
            found = True
            break
    if not found:
        inventory.append({"barang": update["barang"], "jumlah": update["perubahan"]})

with open(fileName, mode="w", newline="") as file:
    csvWriter = csv.writer(file)
    for item in inventory:
        csvWriter.writerow([item["barang"], item["jumlah"]])

print("Inventaris berhasil diperbarui.")
for i in inventory:
    print(i)
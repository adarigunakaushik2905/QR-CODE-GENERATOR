import qrcode

while True:
    print("\n1. Generate QR")
    print("2. Exit")

    choice = input("Choose: ")

    if choice == "2":
        print("👋 Exiting")
        break

    data = input("Enter text/URL: ")
    img = qrcode.make(data)
    img.save("qr_code.png")

    print("✅ QR Code saved as qr_code.png")

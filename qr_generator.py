import qrcode
import datetime

class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr_code(self, file_name: str, fg_color: str, bg_color: str):
        user_input: str = input('Enter text: ')

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg_color, back_color=bg_color)
            qr_image.save(file_name)

            print(f"QR code was successfully created! ({file_name})")

        except Exception as e:
            print(f"Error: {e}")


def main():
    new_qr = MyQR(size=30, padding=2)
    new_qr.create_qr_code("QR" + (datetime.datetime.now()).strftime("%d%m%Y%H%M%S") + ".png", fg_color="black", bg_color="white")


if __name__ == "__main__":
    main()


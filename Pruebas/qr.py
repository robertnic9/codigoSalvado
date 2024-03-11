import qrcode

# Datos que deseas codificar en el QR
datos_a_codificar = "https://www.youtube.com/watch?v=E7awhxG7mwg"

# Crear un objeto QRCode
codigo_qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Agregar los datos al código QR
codigo_qr.add_data(datos_a_codificar)
codigo_qr.make(fit=True)

# Crear una imagen QRCode
imagen_qr = codigo_qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen QRCode
imagen_qr.save("codigo_qr.png")
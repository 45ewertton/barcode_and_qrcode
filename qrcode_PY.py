import qrcode


''' Criação de qrcode não automatizada
image_qrcode = qrcode.make("https://www.youtube.com/watch?v=4mjc5vyxD8E")
image_qrcode.save("qrcode_python.png")
'''
# Criação de qrcode de forma automatizada
favorite_songs = {
    "Three Days Grace": "https://www.youtube.com/watch?v=pwGS4Yn5qLo",
    "Capital Inicial": "https://www.youtube.com/watch?v=IGM-2eO7b_o",
    "Djonga": "https://www.youtube.com/watch?v=VO0f5Q99BD8"
}

for songs in favorite_songs:
    link = favorite_songs[songs]
    image_qrcode = qrcode.make(link)
    image_qrcode.save(f"qrcode_{songs}.png")
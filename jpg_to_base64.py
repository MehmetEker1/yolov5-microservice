import base64
import os

# Mevcut çalışma dizinine göre göreli yollar kullan
base_dir = os.getcwd()
images_dir = os.path.join(base_dir, 'images')
encoded_dir = os.path.join(base_dir, 'encoded_images')

# Eğer encoded_images klasörü yoksa oluştur
if not os.path.exists(encoded_dir):
    os.makedirs(encoded_dir)

while True:
    yol = input("Images klasörü içerisinden isim aynı olmak şartıyla fotoğraf seçin: ")
    image_path = os.path.join(images_dir, f'{yol}.jpg')

    if not os.path.exists(image_path):
        print("Hata: Seçilen dosya Images klasörü içinde bulunamadı. Lütfen geçerli bir dosya ismi girin.")
        continue

    output_path = os.path.join(encoded_dir, f'encoded_image_{yol}.txt')

    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    with open(output_path, 'w') as output_file:
        output_file.write(encoded_string)

    print(f"Base64 kodu {output_path} dosyasına yazıldı.")
    cikis = input("Çıkmak istemiyorsanız Herhangi bir tuşu, programı sonlandırmak için 'e' veya 'E' tuşlayın: ")
    if cikis.lower() == 'e':
        break
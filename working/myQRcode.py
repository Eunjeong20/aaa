import qrcode

qr_data = 'ejchoi@kmh.hs.kr'
qr_img = qrcode.make(qr_data)

save_path = 'QRcode\\' + qr_data + '.png'

qr_img.save(save_path)
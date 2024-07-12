from stegano import lsb



secret = lsb.hide('kup.jpg', 'What the fuck are you doing?')
secret.save('secret.jpg')
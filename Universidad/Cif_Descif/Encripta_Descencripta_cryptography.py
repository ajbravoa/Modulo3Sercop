from cryptography.fernet import Fernet

texto= "P@ssw3rd"

#-----AQUI SE GENERA LA CLAVE EN FORMATO DE SECUENCIA DE BYTES----
key=Fernet.generate_key()
objeto_cifrado=Fernet(key)
texto_encriptado=objeto_cifrado.encrypt(str.encode(texto))

print(texto_encriptado)

texto_descrencripta_bytes=objeto_cifrado.decrypt(texto_encriptado)
print(texto_descrencripta_bytes)

texto_descrencripta=texto_descrencripta_bytes.decode()
print("TEXTO EN CLARO: "+str(texto_descrencripta))





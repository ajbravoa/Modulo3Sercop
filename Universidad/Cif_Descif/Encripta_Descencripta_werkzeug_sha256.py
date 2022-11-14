#----LIBRERIAS 
from werkzeug.security import generate_password_hash, check_password_hash

#def contenido(self, texto):
# valor=None
# return valor

#-----POST-------
mensaje="P@ssw3rd"
texto_encripta=generate_password_hash(mensaje, 'sha256')
print ("=======TEXTO ENCRIPTADO========")
print(texto_encripta)


#------POST (AUTENTICACION)---------
mensaje_entrada="P@ssw3rd"
print(check_password_hash(texto_encripta, mensaje_entrada))




from passlib.context import CryptContext

#ROUND: ITERACCION PARA REDUCIR LA POSIBILIDAD DE CRACKING
contexto= CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000

)

contrasena="P@ssw3rd"
texto_encriptado=contexto.hash(contrasena)
print("CONTRASEÑA ENCRIPTADO: "+texto_encriptado)

#------VERIFICAR LA CONTRASENA---
print(contexto.verify(contrasena,texto_encriptado))



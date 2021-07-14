#IMPORTO LA BIBLIOTECA
import instaloader

#LLAMO AL USUARIO
ig = instaloader.Instaloader()
acc = input("Usuario de Instagram: ")

#DESCARGO LA FOTO
ig.download_profile(acc, profile_pic_only=True)
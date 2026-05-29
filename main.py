def yarat_txt_fayl():
    fayl_ismi = input("Fayl nomini kiriting: ")
    fayl = open(fayl_ismi + ".txt", "w")
    fayl.close()

yarat_txt_fayl()

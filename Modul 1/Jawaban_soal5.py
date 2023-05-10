if __name__ == '__main__' :
    # Tulislah Jawaban

    JarakKota = 120
    KecepatanA = 60
    KecepatanB = 40
    JamBerangkat = 9

    TotalWaktu = ((JarakKota/(KecepatanA + KecepatanB ))*60)
    JamBertemu = JamBerangkat + (TotalWaktu//60)
    MenitBertemu = (TotalWaktu%60)

    print (f" Akan Bertabrakan pada jam {JamBertemu} lebih {MenitBertemu} menit")
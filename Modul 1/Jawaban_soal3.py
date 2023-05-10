if __name__ == '__main__' :
    # Tulislah Jawaban
        jumlah_hari = 485

        tahun = jumlah_hari//360
        bulan = (jumlah_hari%360)//30
        minggu = ((jumlah_hari%360)%30)//7
        hari = (((jumlah_hari%360)%30)%7)

        print(f' {jumlah_hari} = {tahun} tahun {bulan} bulan {minggu} minggu {hari} hari')
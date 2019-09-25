class Buah(object):
	def __init__ (self, a, k, m):
		self.apel = a
		self.kelapa = k
		self.mangga = m

	def jumlahBuah(self):
		return self.apel + self.kelapa + self.mangga

	def cetakData(self):
		print("Apel\t: ", self.apel)
		print("Kelapa\t: ", self.kelapa)
		print("Mangga\t: ", self.mangga)

	def cetakJB(self):
		print("Total dari semua buah diatas\t= ", self.jumlahBuah())

class WarnaBuah(Buah):
	def __init__(self, a, k, m, w):
		self.apel = a 
		self.kelapa = k 
		self.mangga = m 
		self.warna = w 
	def cetakData(self):
		print("Apel\t: ", self.apel)
		print("Kelapa\t: ", self.kelapa)
		print("Mangga\t: ", self.mangga)
		print("Warna dari semua buah tersebut adalah", self.warna)

def main():
	wb1 = WarnaBuah (16, 4, 40, "biru")

	wb1.cetakData()
	wb1.cetakJB()

if __name__ == "__main__":
	main()

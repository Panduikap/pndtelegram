from kimin.Core_Prepare import Prepare
from kimin.Core_Parser import Parser
from kimin.Core_ext import Core_Ext
from kimin.Core_Scraping import Notifikasi
from colorama import Fore, Back, Style

import time, sys, os, threading

with open('token.min','r') as dataku:
	d1 = dataku.read()
token = d1
global stats
stats = []

def Parsing(url):
	hasil = []
	for i in url:
		if not i in hasil:
			print(i)
			hasil.append(i)
	return hasil

def Cleaning(text):
	hasil = ''
	for i in text:
		if i.isnumeric():
			hasil = hasil + i
	return int(hasil)

def Phase2(url, nama, harga, stock):
	time.sleep(1)
	if url.find('shopee.co.id') == -1:
		if stock.lower().find('kosong') == -1:
			if stock.lower().find('habis') == -1:
				temp = f"{url}||{stock}"
				if not temp in stats:
					stats.append(temp)
					cos = Notifikasi(token)
					text = f"===============\nNama Produk : {nama}\nHarga : {harga}\nStok : {stock}\n===============\n\n\nLink Produk : {url}"
					cos.Kirim_Pesan(text)
	else:
		if not stock is None:
			stock = Cleaning(stock)
			temp = f"{url}||{stock}"
			if stock > 0 and not temp in stats:
				stats.append(temp)
				cos = Notifikasi(token)
				text = f"===============\nNama Produk : {nama}\nHarga : {harga}\nStok : {stock}\n===============\n\n\nLink Produk : {url}"
				cos.Kirim_Pesan(text)
	
	print(Fore.YELLOW+'='*50)
	print(f'{Fore.LIGHTBLUE_EX}URL Produk   : {url}')
	print(f"{Fore.LIGHTBLUE_EX}Nama Produk  : {nama}")
	print(f"{Fore.LIGHTBLUE_EX}Harga Produk : {harga}")
	print(f"{Fore.LIGHTBLUE_EX}Stok Produk  : {stock}")
	print(Fore.YELLOW+'='*50)

def Phase1(url):
	browser = 'firefox'
	browser_path='C:/Program Files/Mozilla Firefox/firefox.exe'
	print(Fore.GREEN +'Membuka Driver', end='\r')
	sin =Prepare(url=url, browser=browser, browser_path=browser_path, driver_path='geckodriver.exe', profil_path='profil')
	driver = sin.driver
	time.sleep(1)
	for i in url:
		no = 0
		for a in range(10):
			sin.url = i
			print(Fore.GREEN +'Menset Url!       ', end='\r')
			time.sleep(1)
			print(Fore.GREEN +'Membuka Url!      ', end='\r')
			sin.Visit(driver)
			Core_Ext.tunggu_halaman(driver, i)
			time.sleep(5)
			print(Fore.GREEN +'Mengambil Data!   ', end='\r')
			harga = Parser.GetHarga(driver, i)
			nama = Parser.GetNama(driver, i)
			stock = Parser.GetStock(driver, i)
			if harga is None or nama is None or stock is None:
				print(Fore.RED + 'Ada Masalah Di Stabilitas Koneksi Internet')
				print(Fore.GREEN + 'Mengulangi Proses!', end='\r')

			else:
				Phase2(i, nama, harga, stock)
				break
			no +=1
		if no == 10:
			print(Fore.RED + 'Ada Masalah Koneksi Internet Pada Komputer')
		

	sin.driver.quit()

def Main():
	for i in range(99**99):
		os.system('cls')
		print(Fore.GREEN + 'Menyiapkan Url  ', end='\r')
		with open('url.min','r') as dataku:
			url = dataku.read().splitlines()
		time.sleep(1)
		url = Parsing(url)
		Phase1(url)
		for i in range(60):
			print(f'{Fore.WHITE}{60-(i+1)} {Fore.BLUE}Detik Lagi Sebelum Scraping', end='\r')
			time.sleep(1)

c1 = threading.Thread(target=Main, args=(), kwargs={})
c1.start()
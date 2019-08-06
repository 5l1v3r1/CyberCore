#!/usr/bin/env python

import os

os.system("CyberCore Auto Pentest Framework")

print("""
CyberCore Otomatik Pentest Aracina Hosgeldiniz!

- Bilgi Toplama
1) TCP Port Tarama
2) Isletim Sistemi Tespiti
3) UDP port tespiti
4) Port Versiyon Tespiti
5) Subdomain tespiti
6) Domain Haritasi

- Zafiyet Tarama
7) Kapsamli Tarama
8) Hizli Tarama
9) Özel Tarama (Yakinda)

- Exploitleme
10) SQL Inj
11) Wordpress
12) Joomla
13) Exploit Arama

- Sifre Kirma
14) MD5 Kirma


""")

islemno = raw_input("Islem Numarasi Giriniz")

if(islemno=="1")
              hedefip = raw_input("Hedef Ip Girin: ")

os.system ("nmap" + hedefip)

elif(islemno=="2")

              hedefip = raw_input("Hedef Ip Girin")

os.system("nmap -O " + hedefip)

elif(islemno=="3")

                hedefip = raw_input("Hedef Ip Girin")

os.system("nmap -sS -sV" + hedefip)

elif(islemno=="4")

                hedefip = raw_input("Hedef Ip Girin")

        os.system("nmap -sS -sV " + hedefip)

elif(islemno=="5")

                hedefsite = raw_input("Hedef Site Giriniz")

        os.system("dnsrecon -d " + hedefsite)

elif(islemno=="6")

                hedefsite = raw_input("Hedef Site Giriniz")

        os.system("dnsmap " + hedefsite)

elif(islemno=="7")
                dizin = raw_input("Bos Bir Dizin Girin")
                hedefsite = raw_input("Hedef Site Giriniz")

        os.system("skipfish -o " + dizin + hedefsite)

elif(islemno=="8")

                hedefsite = raw_input("Hedef Site Giriniz")

        os.system("nikto -h " + hedefsite)

elif(islemno=="9")

print ("Bu ozellik gecici olarak kullanima kapalidir.")


elif(islemno=="10")

                hedefsite = raw_input("Zafiyetli Adresi Giriniz")

        os.system("sqlmap -u " + hedefsite " --random-agent --dbs")


elif(islemno=="11")

                hedefsite = raw_input("Hedef Site Giriniz")

                os.system("wpscan --url " + hedefsite)


elif(islemno=="12")

                hedefsite = raw_input("Hedef Site Giriniz")

        os.system("joomscan -u " + hedefsite)

elif(islemno=="13")

        hedefkelime = raw_input("Anahtar Kelime Girin")

os.system("searchsploit " + hedefkelime)

elif(islemno=="14")

                print ("Bu ozellik gecici olarak kullanima kapalidir.")

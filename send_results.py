import os, bs4, requests, random
import smtplib


response = requests.get('https://www.lutrija.rs/Results')
soup = bs4.BeautifulSoup(response.text, "html.parser")

# My generated numbers
my_numbers = set()
while len(my_numbers) < 7:
    my_numbers.add(random.randint(1, 40))

# Numbers from the draw
results = soup.find_all("div", "Rez_Brojevi_Txt_Gray")

# Append numbers to the list
draw = []
for number in results[:7]:
	draw.append(int(number.string))

# Find matching numbers
correct = sum(number in draw for number in my_numbers)

my_numbers = (sorted(my_numbers))
draw = (sorted(draw))
total = f"Pogodio si {correct} od 7!"

try:
	# Send result to email
	conn = smtplib.SMTP('smtp.gmail.com', 587) # connect to email provider - this case - mailfence
	conn.ehlo() # connect
	conn.starttls() # start encryption
	conn.login('psychobuddha.webdev@gmail.com', 'rimsxurwmbfruzhk') # login to account
	conn.sendmail('psychobuddha.webdev@gmail.com', 'denisjovic@pm.me', f"'Subject: Loto results\n\n Moji brojevi: {my_numbers}\n Izvuceni brojevi: {draw}\n Rezultat: {total}'")
	conn.sendmail('psychobuddha.webdev@gmail.com', 'denis.jovic@tn-tech.co.rs', f"'Subject: Loto results\n\n Moji brojevi: {my_numbers}\n Izvuceni brojevi: {draw}\n Rezultat: {total}'")
	conn.quit() # disconnect from the server
	print("Success!")
except:
	print("Something went wrong with email sending")





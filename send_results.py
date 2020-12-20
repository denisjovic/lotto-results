import bs4
import requests
import random
import smtplib


response = requests.get('https://www.lutrija.rs/Results')
soup = bs4.BeautifulSoup(response.text, "html.parser")

# Generate random numbers
my_numbers = set()
while len(my_numbers) < 7:
    my_numbers.add(random.randint(1, 40))

# Numbers from the draw
results = soup.find_all("div", "Rez_Brojevi_Txt_Gray")

draw = []
for number in results[:7]:
	draw.append(int(number.string))

# Find matching numbers
correct = sum(number in draw for number in my_numbers)

my_numbers = (sorted(my_numbers))
draw = (sorted(draw))
total = f"You have got {correct} out of 7!"

try:
	# Send result to email
	conn = smtplib.SMTP('smtp.gmail.com', 587) # connect to email provider
	conn.ehlo() # connect
	conn.starttls() # start encryption
	conn.login( 'email@gmail.com', 'yourpasswordhere') # login to account
	conn.sendmail('email@gmail.com', 'target@email.com', f"'Subject: Loto results\n\n My numbers: {my_numbers}\n Official numbers: {draw}\n Result: {total}'")
	conn.quit() # disconnect from the server
	print("Success!")
except:
	print("Something went wrong with email sending")
	
	
	
# Cron job has been set to run the script twice a week, every Tuesday and Friday





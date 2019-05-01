import sqlite3

def create_event():
	event_name = input("Enter Name of Event: \n")

	while(event_name == ""):
		event_name = input("Do you Really want an empty name for your Event!: \n")

	con = sqlite3.connect('fest.db')
	check = con.execute("SELECT Event_name From events WHERE Event_name = ?", (event_name,))
	check = check.fetchone()

	while (check is not None):
		event_name = input("Event Already Exists. Enter Again: \n")
		check = con.execute("SELECT Event_name From events WHERE Event_name = ?", (event_name,))
		check = check.fetchone()
	

	print("\nChoose Date of Event: ")
	print("Enter 1 for April 20, 2019")
	print("Enter 2 for April 21, 2019")

	date = input()

	while(True):
		if (not date.isdigit()):
			print("Please Enter valid input!!")
			date = input()
			continue
		elif (int(date)<1 or int(date)>2):
			print("Please Enter valid input!!")
			date = input()
			continue
		break

	if (int(date) == 1):
		date = "April 20, 2019"
	else:
		date = "April 21, 2019"

	team = input("Enter team size (1 for solo event): \n")
	while(True):
		if (not team.isdigit()):
			print("Please Enter valid input!!")
			team = input()
			continue
		elif (int(team)<1):
			print("Please Enter valid input!!")
			team = input()
			continue
		team = int(team)
		break
		

	entry = input("Enter entry_fee for event (0 for no fee): \n")

	while(True):
		if (not entry.isdigit()):
			print("Please Enter valid input!!")
			entry = input()
			continue
		elif (int(entry)<0):
			print("Please Enter valid input!!")
			entry = input()
			continue
		entry = int(entry)
		break

	prize = input("Enter prize_MONEY for event ,0 for no prize money:( \n")

	while(True):
		if (not prize.isdigit()):
			print("Please Enter valid input!!")
			prize = input()
			continue
		elif (int(prize)<0):
			print("Please Enter valid input!!")
			entry = input()
			continue
		prize = int(prize)
		break


	material = input("Enter Material Required (Leave Empty for nothing): \n")

	location = input("Enter a location: \n")
	if (location ==""):
		print("Enter a location please: ")
		location = input()

	print("\nHERE IS YOUR FINAL DATA, which you can't edit now :p\n")

	print("Event_name: " + event_name)
	print("Event_date: " + date)
	print("Team_size: " + str(team))
	print("Entry_fee: " + str(entry))
	print("Prize_money: " + str(prize))
	print("Material_Required: " + material) 
	print("Location: " + location + "\n")

	final = (event_name, date, team, entry, prize, material, location)
	con.execute('''INSERT INTO events(Event_name, event_date, team_size, entry_fee, prize_money, material_required, location)
				VALUES(?,?,?,?,?,?,?)''', final)
	con.commit()
	con.close()

	print("\nWait You need to add at least one organizer to your Event, Let Go! \n")
	create_organizer(event_name, "")

	print("\nLets add initial publicity details for event")
	create_publicity(event_name)

	print("\nAdd sponsorship details")
	create_spons(event_name)

def create_team():
	team_name = input("Enter Name of Team: \n")

	while(team_name == ""):
		team_name = input("Do you Really want an empty name for your Team!: \n")

	con = sqlite3.connect('fest.db')
	check = con.execute("SELECT Team_name From teams WHERE Team_name = ?", (team_name,))
	check = check.fetchone()

	while (check is not None):
		team_name = input("Team Already Exists. Enter Again: \n")
		check = con.execute("SELECT Team_name From teams WHERE Team_name = ?", (team_name,))
		check = check.fetchone()

	head_name = input("Enter Head name for the team: \n")

	while(head_name == ""):
		head_name = input("Enter some name: \n")

	budget = input("Enter a positive budget for the team: (0 for no budget): \n")

	while(True):
		if (not budget.isdigit()):
			print("Please Enter valid input!!")
			budget = input()
			continue
		elif (int(budget)<0):
			print("Please Enter valid input!!")
			budget = input()
			continue
		budget = int(budget)
		break

	print("\nHERE IS YOUR FINAL DATA, which you can't edit now :p\n")

	print("Team_name: " + team_name)
	print("Head_name: " + head_name)
	print("Budget: " + str(budget) + "\n")

	final = (team_name, head_name, budget)
	con.execute(con.execute('''INSERT INTO teams(Team_name, head_name, budget)
				VALUES(?,?,?s)''', final))
	con.commit()
	con.close()

	print("\nWait You need to add at least one organizer to your Event, Let Go! \n")
	create_organizer("", team_name)



def create_organizer(event_name, team_name):

	first_name = input("Enter first name of Organizer: \n")

	while(first_name == ""):
		first_name = input("Enter some first_name: \n")


	last_name = input("Enter last name of Organizer: \n")

	while(last_name == ""):
		last_name = input("Enter some last_name: \n")


	cno = input("Enter contact number of the Organizer : \n")

	while(True):
		if (not cno.isdigit()):
			print("Please Enter valid input!!")
			cno = input()
			continue
		elif (int(cno)<0):
			print("Please Enter valid input!!")
			cno = input()
			continue
		cno = int(cno)
		break


	if (event_name!=""):
		print("\nHERE IS YOUR FINAL DATA, which you can't edit now :p\n")

		print("First_name: " + first_name)
		print("Last_name: " + last_name)
		print("Contact_no: " + str(cno))
		print("Event_name: " + event_name + "\n")
		
		final = (first_name, last_name, cno, event_name)
		con = sqlite3.connect('fest.db')
		con.execute('''INSERT INTO organizers(first_name, last_name, contact_no, Event_name)
					VALUES(?,?,?,?)''', final)
		con.commit()
		con.close()


	elif (team_name!=""):
		print("\nHERE IS YOUR FINAL DATA, which you can't edit now :p\n")

		print("First_name: " + first_name)
		print("Last_name: " + last_name)
		print("Contact_no: " + str(cno))
		print("Team_name: " + team_name + "\n")
		
		final = (first_name, last_name, cno, team_name)
		con = sqlite3.connect('fest.db')
		con.execute('''INSERT INTO organizers(first_name, last_name, contact_no, Team_name)
					VALUES(?,?,?,?)''', final)
		con.commit()
		con.close()

	else:
		print("Enter 1 to add organizer to an Event!")
		print("Enter 2 to add organizer to a Team!")

		i = input()

		while(True):
			if (not i.isdigit()):
				print("Please Enter valid input!!")
				i = input()
				continue
			elif (int(i)<1 or int(i)>2):
				print("Please Enter valid input!!")
				i = input()
				continue
			break
		i = int(i)
		
		if (i==1):
			print("\nChoose from given events: \n")

			con = sqlite3.connect('fest.db')
			check = con.execute("SELECT Event_name From events")

			for e in check:
				print(e[0])

			event_name = input()

			check = con.execute("SELECT Event_name From events WHERE Event_name = ?", (event_name,))
			check = check.fetchone()

			while(event_name == ""):
				event_name = input("Please choose from given events: \n")

			while (check is None):
				event_name = input("Please choose from given events: \n")
				check = con.execute("SELECT Event_name From events WHERE Event_name = ?", (event_name,))
				check = check.fetchone()

			print("\nHERE IS YOUR FINAL DATA, which you can't edit now :p\n")

			print("First_name: " + first_name)
			print("Last_name: " + last_name)
			print("Contact_no: " + str(cno))
			print("Event_name: " + event_name + "\n")

			final = (first_name, last_name, cno, event_name)
			con.execute('''INSERT INTO organizers(first_name, last_name, contact_no, Event_name)
					VALUES(?,?,?,?)''', final)
			con.commit()
			con.close()

		else:
			print("\nChoose from given teams: \n")

			con = sqlite3.connect('fest.db')
			check = con.execute("SELECT Team_name From teams")

			for e in check:
				print(e[0])

			team_name = input()

			check = con.execute("SELECT Team_name From teams WHERE Team_name = ?", (team_name,))
			check = check.fetchone()

			while(team_name == ""):
				team_name = input("Please choose from given teams: \n")

			while (check is None):
				team_name = input("Please choose from given teams: \n")
				check = con.execute("SELECT Team_name From teams WHERE Team_name = ?", (team_name,))
				check = check.fetchone()

			print("\nHERE IS YOUR FINAL DATA, which you can't edit now :p\n")

			print("First_name: " + first_name)
			print("Last_name: " + last_name)
			print("Contact_no: " + str(cno))
			print("Team_name: " + team_name + "\n")

			final = (first_name, last_name, cno, team_name)
			con.execute('''INSERT INTO organizers(first_name, last_name, contact_no, Team_name)
					VALUES(?,?,?,?)''', final)
			con.commit()
			con.close()


def create_participant():

	pname = input("\nEnter name of participant: \n")
	while(pname == ""):
		pname = input("Enter some name: \n")

	sc = input("Enter name of school/college of partipant: \n")
	while(sc == ""):
		sc = input("Enter some input: \n")

	cno = input("Enter contact number of the Participant : \n")

	while(True):
		if (not cno.isdigit()):
			print("Please Enter valid input!!")
			cno = input()
			continue
		elif (int(cno)<0):
			print("Please Enter valid input!!")
			cno = input()
			continue
		cno = int(cno)
		break

	email = input("Enter email id of participant: \n")
	while(email == ""):
		email = input("Enter some input: \n")


	con = sqlite3.connect('fest.db')
	check = con.execute("SELECT Participant_name From participants WHERE contact_no = ?", (cno,))
	check = check.fetchone()

	if (check is None):
		final_participant = (pname, sc, cno, email)
		con.execute('''INSERT INTO participants(Participant_name, school_college, contact_no, email_id)
				VALUES(?,?,?,?)''', final_participant)
		con.commit()
		con.close()

	print("\nChoose from given events: \n")

	con = sqlite3.connect('fest.db')
	check = con.execute("SELECT Event_name From events")

	for e in check:
		print(e[0])

	event_name = input()

	check = con.execute("SELECT Event_name From events WHERE Event_name = ?", (event_name,))
	check = check.fetchone()

	while(event_name == ""):
		event_name = input("Please choose from given events: \n")

	while (check is None):
		event_name = input("Please choose from given events: \n")
		check = con.execute("SELECT Event_name From events WHERE Event_name = ?", (event_name,))
		check = check.fetchone()

	print("\nHERE IS YOUR FINAL DATA, which you can't edit now :p\n")

	print("Participant_name: " + pname)
	print("School/College: " + sc)
	print("Contact_no: " + str(cno))
	print("Email_id: " + email)
	print("Event_name: " + event_name + "\n")

	final = (event_name, pname)
	con.execute('''INSERT INTO event_participant(Event_name, Participant_name)
				VALUES(?,?)''', final)
	con.commit()
	con.close()

def create_publicity(event_name):

	online_reach = input("Enter online reach of event: \n")
	while(True):
		if (not online_reach.isdigit()):
			print("Please Enter valid input!!")
			online_reach = input()
			continue
		elif (int(online_reach)<0):
			print("Please Enter valid input!!")
			online_reach = input()
			continue
		online_reach = int(online_reach)
		break

	onground_reach = input("Enter onground reach of event: \n")
	while(True):
		if (not onground_reach.isdigit()):
			print("Please Enter valid input!!")
			onground_reach = input()
			continue
		elif (int(onground_reach)<0):
			print("Please Enter valid input!!")
			onground_reach = input()
			continue
		onground_reach = int(onground_reach)
		break

	posters = input("Enter posters required for event: \n")
	while(True):
		if (not posters.isdigit()):
			print("Please Enter valid input!!")
			posters = input()
			continue
		elif (int(posters)<0):
			print("Please Enter valid input!!")
			posters = input()
			continue
		posters = int(posters)
		break

	final = (event_name, online_reach, onground_reach, posters)
	con = sqlite3.connect('fest.db')
	con.execute('''INSERT INTO publicity_details(Event_name, online_reach, onground_reach, posters)
				VALUES(?,?,?,?)''', final)
	con.commit()
	con.close()


def create_spons(event_name):
	cname = input("\nEnter Company name giving spons: \n")

	while(cname == ""):
		cname = input("Enter some input: \n")

	con = sqlite3.connect('fest.db')
	check = con.execute("SELECT Company_name From sponsorships WHERE Company_name = ?", (cname,))
	check = check.fetchone()

	while(check is not None):
		cname = input("Company Already Exists. Enter Again: \n")
		check = con.execute("SELECT Company_name From sponsorships WHERE Company_name = ?", (cname,))
		check = check.fetchone()

	level = input("Enter level of spons(1,2,3): \n")
	while(True):
		if (not level.isdigit()):
			print("Please Enter valid input!!")
			level = input()
			continue
		elif (int(level)<1 or int(level)>3):
			print("Please Enter valid input!!")
			level = input()
			continue
		level = int(level)
		break

	final_company = (cname, event_name, level)
	con.execute('''INSERT INTO sponsorships(Company_name, Event_name, level)
				VALUES(?,?,?)''', final_company)

	print("Enter y to add some requirements(may be a stall): \n")
	y = input()

	if (y == "y"):
		no = input("Enter number of requirements: \n")
		while(True):
			if (not no.isdigit()):
				print("Please Enter valid input!!")
				no = input()
				continue
			elif (int(no)<0):
				print("Please Enter valid input!!")
				no = input()
				continue
			no = int(no)
			break

		for i in range(no):
			req = input("Enter the requirement: \n")
			if (req==""):
				req = input("Enter some requirement: \n")
			final_req = (req, cname)
			con.execute('''INSERT INTO other_requirements(requirement, Company_name)
				VALUES(?,?)''', final_req)

	print("Enter y to add some inkind/cash: \n")
	y = input()

	if (y == "y"):
		no = input("Enter number of inputs: \n")
		while(True):
			if (not no.isdigit()):
				print("Please Enter valid input!!")
				no = input()
				continue
			elif (int(no)<0):
				print("Please Enter valid input!!")
				no = input()
				continue
			no = int(no)
			break

		for i in range(no):
			ink = input("Enter the input: \n")
			if (ink==""):
				ink = input("Enter some input: \n")
			final_ink = (ink, cname)
			con.execute('''INSERT INTO inkind_cash(inkind, Company_name)
				VALUES(?,?)''', final_ink)

	con.commit()
	con.close()





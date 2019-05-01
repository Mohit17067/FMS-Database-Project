import sqlite3

def get_cnos():
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

	participants = con.execute("SELECT Participant_name from event_participant WHERE Event_name = ?", (event_name,))

	print("\nHere is the output, if any: ")
	for p in participants:
		pname = p[0]
		cno = con.execute("SELECT contact_no FROM participants WHERE Participant_name = ?", (pname,))
		for c in cno:
			print("Participant_Name: " + pname + "  Contact Number: " + str(c[0]))
	con.close()

def get_maxonline():
	con = sqlite3.connect('fest.db')

	events = con.execute("SELECT Event_name, online_reach FROM publicity_details WHERE online_reach = (SELECT max(online_reach) FROM publicity_details)")

	print("\nHere is(are) the Event(s) with maximum online reach, if any: ")

	for e in events:
		print("Event_name: " + e[0] + " Online_Reach: " + str(e[1]))
	con.close()

def get_levelx():

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

	print("\nHere are the name of companies providing level " + str(level) + " sponsorships: ")

	con = sqlite3.connect('fest.db')
	companies = con.execute("SELECT Company_name FROM sponsorships WHERE level = ?", (level,))

	for c in companies:
		print(c[0])
	con.close()

def get_orgteam():
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

	orgs = con.execute("SELECT first_name, last_name FROM organizers WHERE Team_name = ?", (team_name,))

	print("\nHere are the names of all organizers in team " + team_name)
	for o in orgs:
		print("Name: " + o[0]+" " +o[1]) 
	con.close()

def update_loc():
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


	location = input("Enter a new location: \n")
	if (location ==""):
		print("Enter a location please: ")
		location = input()

	con.execute("UPDATE events set location = ? WHERE Event_name = ?", (location, event_name,))
	print("Location Update Successfully!")
	con.commit()
	con.close()

def count_event():
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

	count = con.execute("SELECT count(*) FROM event_participant WHERE event_name = ?", (event_name,))

	for c in count:
		print("Number of participants of Event: " + event_name + " : " + str(c[0]))

	con.close()


def no_publicity():
	print("Here are the events who do no require any publicity, if any: \n")

	con = sqlite3.connect('fest.db')
	check = con.execute("SELECT Event_name FROM events WHERE Event_name NOT IN (SELECT Event_name FROM Publicity_Details) ")

	for e in check:
		print("Event_name: " + e[0] + "\n")

	con.close()

def invalid_email():

	con = sqlite3.connect('fest.db')
	check = con.execute("SELECT Participant_name,contact_no,email_id FROM PARTICIPANTS WHERE email_id NOT LIKE '%_@__%.__%'")

	print("Participants with invalid Email_id, if any: \n")

	for p in check:
		print("Participant_name: " + p[0] + " Contact_no: " + str(p[1]) + " Email_id: " + p[2] + "\n")

	con.close()

def event_organizers():
	con = sqlite3.connect('fest.db')
	check = con.execute("SELECT organizers.Event_name, first_name, last_name FROM organizers INNER JOIN events ON organizers.Event_name==events.Event_name")


	print("Event Organizers: \n")
	for x in check:
		print("Event_name: " + x[0] + "Organizer_name: " + x[1] + " " + x[2]);

	con.close()
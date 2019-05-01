import sqlite3

def view_events():
	con = sqlite3.connect('fest.db')

	###   DETAILS OF EVENTS   ###
	events = con.execute("SELECT * FROM events")

	print("Here are the details of all Events :\n")

	event_widths = {0:len("Event_name"),1:len("Date"),2:len("Team_size"),3:len("Entry_fee"), 4:len("Prize"), 5:len("Material"), 6:len("Location")}
	for e in events:
		for i,v in enumerate(e):
			event_widths[i] = max(event_widths[i], len(str(v)))

	events = con.execute("SELECT * FROM events")
	name, date, size, fee, prize , mat, loc = ["Event_name", "Date", "Team_size", "Entry_fee", "Prize", "Material", "Location"]
	print(f"{name:<{event_widths[0]}}  |  {date:<{event_widths[1]}}  |  {size:<{event_widths[2]}}  |  {fee:<{event_widths[3]}}  |  {prize:<{event_widths[4]}}  |  {mat:<{event_widths[5]}}  |  {loc:<{event_widths[6]}}")

	print("-" * (event_widths[0]+event_widths[1]+event_widths[2]+event_widths[3]+event_widths[4]+event_widths[5]+event_widths[6]+20))
	for e in events:
		name, date, size, fee, prize , mat, loc = e
		print(f"{name:<{event_widths[0]}}  |  {date:<{event_widths[1]}}  |  {size:<{event_widths[2]}}  |  {fee:<{event_widths[3]}}  |  {prize:<{event_widths[4]}}  |  {mat:<{event_widths[5]}}  |  {loc:<{event_widths[6]}}")


def view_teams():
	con = sqlite3.connect('fest.db')

	### DETAILS OF TEAMS   ###
	teams = con.execute("SELECT * FROM teams")

	print("\n\nHere is the list of all teams : \n")

	team_widths = {0:len("Team_name"),1:len("Head_name"),2:len("Budget")}
	for e in teams:
		for i,v in enumerate(e):
			team_widths[i] = max(team_widths[i], len(str(v)))

	teams = con.execute("SELECT * FROM teams")
	tname, hname, bud = ["Team_name", "Head_name", "Budget"]
	print(f"{tname:<{team_widths[0]}}  |  {hname:<{team_widths[1]}}  |  {bud:<{team_widths[2]}}")

	print("-" * (team_widths[0]+team_widths[1]+team_widths[2]+10))
	for e in teams:
		tname, hname, bud = e
		print(f"{tname:<{team_widths[0]}}  |  {hname:<{team_widths[1]}}  |  {bud:<{team_widths[2]}}")

	con.close()



def view_organizers():
	con = sqlite3.connect('fest.db')

	### DETAILS OF ORGANIZERS   ###
	organizers = con.execute("SELECT * FROM organizers")

	print("\n\nHere are the details of all Organizers :\n")

	org_widths = {0:len("id"),1:len("first_name"),2:len("last_name"),3:len("contact_no"),4:len("Event_name"), 5:len("Team_name")}
	
	for e in organizers:
		for i,v in enumerate(e):
			if v is not None:
				org_widths[i] = max(org_widths[i], len(str(v)))

	organizers = con.execute("SELECT * FROM organizers")
	ID, fname, lname, cno, ename, tname = ["id", "First_name", "Last_name", "Contact_no", "Event_name", "Team_name"]
	print(f"{ID:<{org_widths[0]}}  |  {fname:<{org_widths[1]}}  |  {lname:<{org_widths[2]}}  |  {cno:<{org_widths[3]}}  |  {ename:<{org_widths[4]}}  |  {tname:<{org_widths[5]}}")

	print("-" * (org_widths[0]+org_widths[1]+org_widths[2]+org_widths[3]+org_widths[4]+org_widths[5]+20))
	for e in organizers:
		ID, fname, lname, cno, ename, tname = e
		if ename is None:
			ename = "No event"
		if tname is None:
			tname = "No team"
		print(f"{ID:<{org_widths[0]}}  |  {fname:<{org_widths[1]}}  |  {lname:<{org_widths[2]}}  |  {cno:<{org_widths[3]}}  |  {ename:<{org_widths[4]}}  |  {tname:<{org_widths[5]}}")

	con.close()


def view_publicity():
	con = sqlite3.connect('fest.db')

	### Publicity Details   ###
	pub = con.execute("SELECT * FROM publicity_details")

	print("\n\nHere is the publicity details of events : ")
	print("NOTE: Some events may have no publicty details\n")

	pub_widths = {0:len("Event_name"),1:len("Online_Reach"),2:len("Onground_reach"),3:len("Posters")}
	for e in pub:
		for i,v in enumerate(e):
			pub_widths[i] = max(pub_widths[i], len(str(v)))

	pub = con.execute("SELECT * FROM publicity_details")
	ename, online, onground, pos = ["Event_name", "Online_reach", "Onground_reach", "Posters"]
	print(f"{ename:<{pub_widths[0]}}  |  {online:<{pub_widths[1]}}  |  {onground:<{pub_widths[2]}}  |  {pos:<{pub_widths[3]}}")

	print("-" * (pub_widths[0]+pub_widths[1]+pub_widths[2]+pub_widths[3]+10))
	for e in pub:
		ename, online, onground,pos = e
		print(f"{ename:<{pub_widths[0]}}  |  {online:<{pub_widths[1]}}  |  {onground:<{pub_widths[2]}}  |  {pos:<{pub_widths[3]}}")

	con.close()

def view_participants():
	con = sqlite3.connect('fest.db')

	### DETAILS OF PARTICIPANTS ###
	participants = con.execute("SELECT * FROM participants")

	print("\n\nHere are the details of all Participants :\n")

	par_widths = {0:len("Participant_name"),1:len("Institute_name"),2:len("Contact_no"),3:len("Email_id"),4:len("Events_name"), 5:len("Team_name")}
	
	for e in participants:
		for i,v in enumerate(e):
			if v is not None:
				par_widths[i] = max(par_widths[i], len(str(v)))

	participants = con.execute("SELECT * FROM participants")
	pname, iname, cno, email,ename = ["Participant_name", "Institute_name", "Contact_no","Email_id", "Events_name"]
	print(f"{pname:<{par_widths[0]}}  |  {iname:<{par_widths[1]}}  |  {cno:<{par_widths[2]}}  |  {email:<{par_widths[3]}}  |  {ename:<{par_widths[4]}}")

	print("-" * (par_widths[0]+par_widths[1]+par_widths[2]+par_widths[3]+par_widths[4]+20))
	for e in participants:
		pname, iname, cno, email = e
		ename = con.execute("SELECT Event_name FROM event_participant WHERE Participant_name=?", (pname,))
		temp = ""
		for e in ename:
			if (temp!=""):
				temp = temp + ", " + e[0]
			else:
				temp = e[0]
		print(f"{pname:<{par_widths[0]}}  |  {iname:<{par_widths[1]}}  |  {cno:<{par_widths[2]}}  |  {email:<{par_widths[3]}}  |  {temp:<{par_widths[4]}}")

	con.close()

def view_spons():
	con = sqlite3.connect('fest.db')
	
	### DETAILS OF SPONSORING COMPANIES ###
	spons = con.execute("SELECT * FROM sponsorships")

	print("\n\nHere are the details of all Sponsorships :\n")

	spons_widths = {0:len("Company_name"),1:len("Event_name"),2:len("Level"),3:len("Other_requirements"),4:len("Inkind_cash")}
	
	for e in spons:
		for i,v in enumerate(e):
			if v is not None:
				spons_widths[i] = max(spons_widths[i], len(str(v)))

	spons = con.execute("SELECT * FROM sponsorships")
	cname, ename, lev, oth, ink = ["Company_name", "Event_name", "Level","Other_Requirements", "Inkind_Cash"]
	print(f"{cname:<{spons_widths[0]}}  |  {ename:<{spons_widths[1]}}  |  {lev:<{spons_widths[2]}}  |  {oth:<{spons_widths[3]}}  |  {ink:<{spons_widths[4]}}")

	print("-" * (spons_widths[0]+spons_widths[1]+spons_widths[2]+spons_widths[3]+spons_widths[4]+20))
	for e in spons:
		cname, ename, lev = e

		other = con.execute("SELECT requirement FROM other_requirements WHERE Company_name=?", (cname,))
		oth = ""
		for e in other:
			if (oth != ""):
				oth = oth + ", " + e[0]
			else:
				oth = e[0]

		inkind = con.execute("SELECT inkind from inkind_cash WHERE Company_name=?", (cname,))
		ink = ""
		for e in inkind:
			if (ink != ""):
					ink = ink + ", " + e[0]
			else:
				ink = e[0]

		print(f"{cname:<{spons_widths[0]}}  |  {ename:<{spons_widths[1]}}  |  {lev:<{spons_widths[2]}}  |  {oth:<{spons_widths[3]}}  |  {ink:<{spons_widths[4]}}")

	con.close()
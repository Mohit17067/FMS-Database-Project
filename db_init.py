import sqlite3

con = sqlite3.connect('fest.db')

###  CREATE TABLES ###


#Create table for Event
con.execute('''CREATE TABLE events
			(Event_name TEXT PRIMARY KEY,
			event_date DATE NOT NULL,
			team_size INT DEFAULT 1,
			entry_fee INT DEFAULT 0,
			prize_money INT DEFAULT 0,
			material_required TEXT DEFAULT NULL,
			location TEXT DEFAULT NULL);''')


#Create table for Teams
con.execute('''CREATE TABLE teams
			(Team_name TEXT PRIMARY KEY,
			head_name TEXT NOT NULL,
			budget INT DEFAULT 0);''')


#Create table for Organizers
con.execute('''CREATE TABLE organizers
			(id INTEGER PRIMARY KEY,
			first_name TEXT NOT NULL,
			last_name TEXT NOT NULL,
			contact_no INT NOT NULL,
			Event_name TEXT,
			Team_name TEXT,
			FOREIGN KEY(Event_name) REFERENCES events(Event_name) ON DELETE SET NULL,
			FOREIGN KEY(Team_name) REFERENCES teams(Team_name) ON DELETE SET NULL);''')


#Create table for participant
con.execute('''CREATE TABLE participants
			(Participant_name TEXT NOT NULL,
			school_college TEXT NOT NULL,
			contact_no INT PRIMARY KEY,
			email_id TEXT NOT NULL);''')


#Create table for event_participant relation
con.execute('''CREATE TABLE event_participant
			(id INT PRIMARY KEY,
			Event_name TEXT NOT NULL,
			Participant_name TEXT NOT NULL,
			FOREIGN KEY(Event_name) REFERENCES events(Event_name) ON DELETE CASCADE,
			FOREIGN KEY(Participant_name) REFERENCES participants(Participant_name) ON DELETE CASCADE);''')


#Create table for sponsorship
con.execute('''CREATE TABLE sponsorships
			(Company_name TEXT NOT NULL,
			Event_name TEXT NOT NULL,
			level INT NOT NULL,
			PRIMARY KEY(Company_name));''')

#Create table for other_requirements, multi-valued arguments for sponsorships
con.execute('''CREATE TABLE other_requirements
			(requirement TEXT ,
			Company_name TEXT NOT NULL,
			PRIMARY KEY(requirement, Company_name),
			FOREIGN KEY(Company_name) REFERENCES sponsorships(Company_name) ON DELETE CASCADE);''')

#Create table for inkind/cash, multivalued arguments for sponsorships
con.execute('''CREATE TABLE inkind_cash
			(inkind TEXT,
			Company_name TEXT NOT NULL,
			PRIMARY KEY(inkind, Company_name),
			FOREIGN KEY(Company_name) REFERENCES sponsorships(Company_name) ON DELETE CASCADE);''')


#Create table for Publicity Details
con.execute('''CREATE TABLE publicity_details
			(Event_name TEXT PRIMARY KEY,
			online_reach INT DEFAULT 0,
			onground_reach INT DEFAULT 0,
			posters INT DEFAULT 0,
			FOREIGN KEY(Event_name) REFERENCES events(Event_name) ON DELETE CASCADE);''')



### ADD INITIAL DATA TO TABLES ###

#Add Events
Events = [('E1', 'April 20, 2019', 2, 50, 1000, 'tapes, scissors, chairs, tables', 'seminar-ground-floor'),
		 ('E2', 'April 21, 2019', 1, 100, 5000, 'mikes, speakers, electricity', 'main-stage'),
		 ('E3', 'April 20, 2019', 1, 0, 1000, 'chart papers, drawing pencils, colors', 'cdx-room')]

con.executemany('''INSERT INTO events(Event_name, event_date, team_size, entry_fee, prize_money, material_required, location)
				VALUES(?,?,?,?,?,?,?)''', Events)


#Add Teams
Teams = [('T1', 'T1H1', 10000), ('T2', 'T2H2', 30000)]

con.executemany('''INSERT INTO teams(Team_name, head_name, budget)
					VALUES(?,?,?)''', Teams)


#Add Organizers
Event_organizers = [('OF1', 'OL1', 1111, 'E2'), ('OF2', 'OL2', 2222, 'E3'), ('OF3', 'OL3', 3333, 'E3'),('OF4', 'OL4', 4444, 'E1')]
Team_organizers = [('OF5', 'OL5', 5555, 'T1'), ('OF6', 'OL6', 6666, 'T2')]

con.executemany('''INSERT INTO organizers(first_name, last_name, contact_no, Event_name)
				VALUES(?,?,?,?)''', Event_organizers)
con.executemany('''INSERT INTO organizers(first_name, last_name, contact_no, Team_name)
				VALUES(?,?,?,?)''', Team_organizers)


#Add Participants
Participants = [('P1', 'SC1', 11111, 'p1@gmail.com'), ('P2', 'SC2', 22222, 'p2@gmail.com'), ('P3', 'SC3', 33333, 'p3@gmail.com'), ('P4', 'SC4', 44444, "Invalid Email")]

con.executemany('''INSERT INTO participants(Participant_name, school_college, contact_no, email_id)
				VALUES(?,?,?,?)''', Participants)


#Add participant-event relationships
participant_event = [('E1', 'P1'), ('E2', 'P2'), ('E3', 'P1'), ('E1', 'P3'), ('E2', 'P4')]

con.executemany('''INSERT INTO event_participant(Event_name, Participant_name)
				VALUES(?,?)''', participant_event)


#Add publicity-details
publicity = [('E1', 10000, 2000, 100), ('E2', 50000, 4000, 200)]

con.executemany('''INSERT INTO publicity_details(Event_name, online_reach, onground_reach, posters)
				VALUES(?,?,?,?)''', publicity)


#Add sponsorships
companies = [('C1', 'E1', 3), ('C2', 'E1', 1), ('C3', 'E2', 2)]
requirements = [('seminar', 'C1'), ('stall', 'C1'), ('app_installs', 'C2'), ('page_likes', 'C2'), ('stall', 'C3')]
inkind = [('goodies worth Rs20000', 'C1'), ('10000 cash', 'C1'), ('coupans worth Rs15000', 'C2'), ('goodies worth Rs10000', 'C3')]

con.executemany('''INSERT INTO sponsorships(Company_name, Event_name, level)
				VALUES(?,?,?)''', companies)
con.executemany('''INSERT INTO other_requirements(requirement, Company_name)
				VALUES(?,?)''', requirements)
con.executemany('''INSERT INTO inkind_cash(inkind, Company_name)
				VALUES(?,?)''', inkind)


con.commit()
con.close()
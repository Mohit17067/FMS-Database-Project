import sqlite3

con = sqlite3.connect('fest.db')

###  CREATE TABLES ###


#Create table for Event
con.execute('''CREATE TABLE events
			(Event_name TEXT,
			event_date DATE NOT NULL,
			team_size INT DEFAULT 1,
			entry_fee INT DEFAULT 0,
			prize_money INT DEFAULT 0,
			material_required TEXT DEFAULT NULL,
			location TEXT DEFAULT NULL,
			PRIMARY KEY(Event_name));''')


#Create table for Teams
con.execute('''CREATE TABLE teams
			(Team_name TEXT,
			head_name TEXT NOT NULL,
			budget INT DEFAULT 0,
			PRIMARY KEY(Team_name));''')


#Create table for Organizers
con.execute('''CREATE TABLE organizers
			(id INT AUTO_INCREMENT,
			first_name TEXT NOT NULL,
			last_name TEXT NOT NULL,
			contact_no INT NOT NULL,
			Event_name TEXT,
			Team_name TEXT,
			PRIMARY KEY(id),
			FOREIGN KEY(Event_name) REFERENCES events(Event_name) ON DELETE SET NULL,
			FOREIGN KEY(Team_name) REFERENCES teams(Team_name) ON DELETE SET NULL);''')


#Create table for participant
con.execute('''CREATE TABLE participants
			(Participant_name TEXT NOT NULL,
			school_college TEXT NOT NULL,
			contact_no INT NOT NULL,
			email_id TEXT NOT NULL,
			PRIMARY KEY(contact_no));''')


#Create table for event_participant relation
con.execute('''CREATE TABLE event_participant
			(id INT AUTO_INCREMENT,
			Event_name TEXT NOT NULL,
			Participant_name TEXT NOT NULL,
			PRIMARY KEY(id),
			FOREIGN KEY(Event_name) REFERENCES events(Event_name) ON DELETE CASCADE,
			FOREIGN KEY(Participant_name) REFERENCES participants(Participant_name) ON DELETE CASCADE);''')

#Create table for sponsorship
con.execute('''CREATE TABLE sponsorships
			(Company_name TEXT NOT NULL,
			Event_name TEXT NOT NULL,
			level INT NOT NULL,
			stall_status TEXT NOT NULL,
			PRIMARY KEY(Company_name, Event_name));''')

#Create table for other_requirements, multi-valued arguments for sponsorships
con.execute('''CREATE TABLE other_requirements
			(requirement TEXT ,
			Company_name TEXT NOT NULL,
			PRIMARY KEY(requirement),
			FOREIGN KEY(Company_name) REFERENCES sponsorships(Company_name) ON DELETE CASCADE);''')

#Create table for inkind/cash, multivalued arguments for sponsorships
con.execute('''CREATE TABLE inkind_cash
			(inkind TEXT,
			Company_name TEXT NOT NULL,
			PRIMARY KEY(inkind),
			FOREIGN KEY(Company_name) REFERENCES sponsorships(Company_name) ON DELETE CASCADE);''')


#Create table for Publicity Details
con.execute('''CREATE TABLE publicty_details
			(online_reach INT DEFAULT 0,
			Event_name TEXT,
			onground_reach INT DEFAULT 0,
			posters INT DEFAULT 0,
			PRIMARY KEY(Event_name),
			FOREIGN KEY(Event_name) REFERENCES events(Event_name) ON DELETE CASCADE);''')



con.close()
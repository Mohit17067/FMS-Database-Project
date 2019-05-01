import sqlite3
from create import *
from view import *
from general import *

def current_structure():
	
	view_events()

	view_teams()

	view_organizers()

	view_participants()

	view_spons()

	view_publicity()




def main():
	print("!!!!!!!!!!! Hii, WELCOME TO FMS !!!!!!!!!!!\n")

	print("Lets see the current data!!\n")
	current_structure()

	while(True):
		print("\n\nWhat Do You Wanna Do ?????")

		print("\nEnter 0 to EXIT !!!")
		print("Enter 1 to Add Stuff !!!")
		print("Enter 2 to View Stuff !!!")
		print("Enter 3 to do some random queries !!!")

		i = input()

		while(True):
			if (not i.isdigit()):
				print("Please Enter valid input!!")
				i = input()
				continue
			elif (int(i)<0 or int(i)>3):
				print("Please Enter valid input!!")
				i = input()
				continue
			i = int(i)
			break

		if (i==0):
			print("BYEEE !!!")
			quit()

		elif (i==1):
			print("\nPlease choose from choices below:\n")

			print("Enter 0 to EXIT !")
			print("Enter -1 to RETURN TO PREVIOUS MENU !")
			print("Enter 1 to Add Event !")
			print("Enter 2 to Create a Team !")
			print("Enter 3 to Add Organizer !")
			print("Enter 4 to Add Participant !")

			j = input()

			while(True):
				if (not j.isdigit() and j!="-1"):
					print("Please Enter valid input!!")
					j = input()
					continue
				elif (int(j)<-1 or int(j)>4):
					print("Please Enter valid input!!")
					j = input()
					continue
				break

			j = int(j)

			if (j==0):
				print("BYEEE !!!")
				quit()
			elif (j==-1):
				continue
			elif (j == 1):
				create_event()
			elif (j == 2):
				create_team()
			elif (j==3):
				create_organizer("", "")
			else:
				create_participant()

		elif (i==2):
			print("\nPlease choose from choices below:\n")

			print("Enter 0 to EXIT !")
			print("Enter -1 to RETURN TO PREVIOUS MENU !")
			print("Enter 1 to view all Events !")
			print("Enter 2 to view all teams !")
			print("Enter 3 to view all organizers!")
			print("Enter 4 to view all participants !")
			print("Enter 5 to view all Sponsorships")


			j = input()

			while(True):
				if (not j.isdigit() and j!="-1"):
					print("Please Enter valid input!!")
					j = input()
					continue
				elif (int(j)<-1 or int(j)>5):
					print("Please Enter valid input!!")
					j = input()
					continue
				break

			j = int(j)

			if (j==0):
				print("BYEEE !!!")
				quit()
			elif (j==-1):
				continue
			elif (j == 1):
				view_events()
			elif (j == 2):
				view_teams()
			elif (j==3):
				view_organizers()
			elif (j==4):
				view_participants()
			else:
				view_spons()

		else:
			print("\nPlease choose from choices below:\n")

			print("Enter 0 to EXIT! ")
			print("Enter -1 to RETURN TO PREVIOUS MENU! ")
			print("Enter 1 to retrieve Contact Nos of participants of an Event! ")
			print("Enter 2 to retrieve Event(s) with maximum online reach!" )
			print("Enter 3 to retrieve Companies providing level_x(1,2,3) Sponsorships! ")
			print("Enter 4 to retrieve First and last names of all organizers in a team! ")
			print("Enter 5 to update location of an Event! ")
			print("Enter 6 to count number of participants of an Event! ")
			print("Enter 7 to get events which do not require any publicity! ")
			print("Enter 8 to view participants with invalid email-ids!")
			print("Enter 9 to view all event_organizers! ")

			j = input()

			while(True):
				if (not j.isdigit() and j!="-1"):
					print("Please Enter valid input!!")
					j = input()
					continue
				elif (int(j)<-1 or int(j)>9):
					print("Please Enter valid input!!")
					j = input()
					continue
				break

			j = int(j)

			if (j==0):
				print("BYEEE !!!")
				quit()
			elif (j==-1):
				continue
			elif (j == 1):
				get_cnos()
			elif (j==2):
				get_maxonline()
			elif (j==3):
				get_levelx()
			elif (j==4):
				get_orgteam()
			elif (j==5):
				update_loc()
			elif (j==6):
				count_event()
			elif (j==7):
				no_publicity()
			elif (j==8):
				invalid_email()
			elif (j==9):
				event_organizers()



if __name__ == '__main__':
	main()
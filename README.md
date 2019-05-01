# FMS-Database-Project
A Fest Management System made with Python.


## Requirement
`Python 3` <br>
`SQLite3 Module`<br>

## How to Run
  * Clone the repository.
  * Create the Database using `python3 db_init.py`
  * Shoot the Application using `python3 app.py`

## ER Diagram
![ER Diagram For Project](https://github.com/Mohit17067/FMS-Database-Project/blob/master/ER_Diagram.png "ER Diagram of Project")<br>

## Objective

Almost every college around the globe organizes different fests throughout the year which makes it imperative to have a system specially designed to ensure proper coordination and smooth functioning of the whole process. We plan to design an interactive system for the management of college fests keeping in mind the different needs for coordination and management. Thus, reducing the total manual effort involved.

The system would have all the information like the events happening and their details, the organizers of the fest, publicity details, details of the participants, the event organizers, Sponsors, etc. Different people using the system would have a different kind of access to the data based on their designation. The emphasis of the project would be on providing an interface that’s easy to use and enhancing the user experience to make the system accessible to almost every college

## Features

**Event** - The main entity of the system will be Event. Its attributes are **Name** (key attribute), **Date** (of the event), **Team Size**, **Entry Fee** (if any), **Prize Money**, **Material Required**(multi-valued attribute) and **Location**. 

**Participant** - Another entity will be a Participant of an event. This is a **weak entity** and is related to an event with a **participates in** relationship. Its attributes are **Name**, **Institute Name**, **Contact number**, and **Email ID**. Every participant must be present in at least one event (total participation) but an event could have 0 participant (partial participation), which could result in cancellation of an event. 

**Organizer** - Entity Organizer has attributes **ID** (key attribute), **Name** (compound attribute with *first_name* and *last_name*) and **Contact Number**. Related to an Event with **manages** relationship. Every event must have at least one organizer (total participation) but an organizer can organize an event or could be present in other teams.

**Team** - Entity Team has attributes **Team Name**, **Head Name**, and **Budget**. Related to Organiser with **contains** relationship. Every team must have at least one organizer (total participation) while an organizer could not be there in any team (partial participation).

**Sponsorship** - Entity Sponsorship has attributes **Company Name** (key attribute), **In-kind/cash**(multi-valued attribute), **Level** (of sponsorship), **Stall Status** (required or not) and **Other requirements** (of a company, maybe a seminar required or not, multi-valued attribute). Related to Event with **Details for** relationship. A “sponsorship” must be related to an event (total participation) but there could be an event with no sponsorship at an instance (partial participation).

**Publicity Details** - Another weak entity Publicity Details related to an event with a weak relationship **associated with**. Attributes are **Online Reach**, **On-ground Reach**, and **Number of posters**. A publicity detail must be associated with an event (total participation) but there could be an event with no publicity required (partial participation).

## Queries

Basic Queries to add and view all data is present.

Complex queries using *Join*, *count*, and other sql operations are present in **random queries section**.

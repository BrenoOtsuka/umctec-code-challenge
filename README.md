# umctec-code-challenge
The challenge is to build an API to post and get activities and cards

# Language and Libraries

- Python 3.8.2
- Flask 1.1.2
- SQLite3 3.31.1

# Project Structure

- main.py creates the routes

- testRepository.py contains the unit tests (To run the unit tests, execute this script)

- miniexamples.py and examples contain the data used in the unit tests in a dictionary format

- database.py contains some functions to create the database

- cardRepository.py and activityRepository.py contain the functions to implement the API


# Instructions to build and run the project

After install Python 3 and Flask, you run the project executing main.py. To send requests to the API, I used Postman. The routes are:

Get all activity : /api/v1/activity/all (GET)
Add activity : /api/v1/activity (POST)
- In the Body 

``` json 
{
    "activityId" : 0 (optional),
    "title": "Centro Cirurgico",
    "subtitle": "Agendar cirurgia",
    "sla": 2
}
```

Get card by : /api/v1/card?q=patientName&filter=PRIORITY
- In the Body

``` json 
{
    "key" : "Graziely Scharf Borelli"
}
```

- q can assume patientName, visitId or billId as value
- filter can assume PRIORITY, TO_RECEIVE or TO_SEND as value

Add card : /api/v1/card (POST)
- In the Body  

``` json 
{
        "patient": {
            "patientID": 0,
            "name": "Fernando Leite Serrano"
        },
        "healthInsurance": {
            "healthInsuranceID": 0,
            "name": "Maxima Seguro"
        },
        "bill": {
            "billID": 0,
            "billType": "HOSPITALAR",
            "numberOfPendencies": 10,
            "numberOfOpenPendencies": 0,
            "totalAmount": 8925.55
        },
        "visitId": 0,
        "slaStatus": "DELAYED",
        "daysSinceCreated": 20,
        "numberOfDocuments": 3,
        "numberOfNotReceivedDocuments": 2,
        "numberOfChecklistItem": 0,
        "numberOfDoneChecklistItem": 0
    }
``

IMPORTANTE: In the requests that uses Body, it is important to specify in the Header that Content-Type is equal to application/json

# Required

- [ ] Create a Java Spring Boot project;
- [ ] Use JPA and Hibernate to persist and get data from a SQL database;
- [ ] You can use in-memory databases like H2 or a server database (MySQL or PostgreSQL);
- [x] Show us your work through your commit history in a new GitHub repository;

# Bonus

- [ ] Document and expose your API with Swagger or alternative;
- [ ] Create sql tables and rows using Flyway or alternative;
- [x] Implement unit tests; (partialy)
- [ ] Implement integration tests;
- [x] Error handling; (partialy)
- [ ] Use spring security to authorize and authenticate the endpoints;
- [x] You can use any library that simplifies your work;
- [ ] Host the API on the service of your choice;

# Endpoints
    
- [x] Get all activities:
- [x] Create activity
- [x] Create card
- [x] Search cards by patientName
- [x] Search cards by visitId
- [x] Search cards by billId
- [x] filter by PRIORITY
- [x] filter by TO_RECEIVE
- [x] filter by TO_SEND
- [x] totalCardsOk: Number of cards (all pages) with slaStatus OK
- [x] totalCardsWarning: Number of cards (all pages) with slaStatus WARNING
- [x] totalCardsDelayed: Number of cards (all pages) with slaStatus DELAYED
- [ ] get cards by activityId
- [ ] pagination

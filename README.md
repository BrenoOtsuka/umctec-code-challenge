# umctec-code-challenge
The challenge is to build an API to post and get activities and cards

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
- [ ] get cards by activityId
- [ ] totalCardsOk: Number of cards (all pages) with slaStatus OK
- [ ] totalCardsWarning: Number of cards (all pages) with slaStatus WARNING
- [ ] totalCardsDelayed: Number of cards (all pages) with slaStatus DELAYED
- [ ] pageInfo: Add any new fields you think is important to build the pagination component in web page
- [ ] filter by perPage: number of elements in each page
- [ ] get by page: index of page

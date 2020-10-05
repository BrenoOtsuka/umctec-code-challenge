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
- [x] Implement unit tests;
- [ ] Implement integration tests;
- [x] Error handling;
- [ ] Use spring security to authorize and authenticate the endpoints;
- [x] You can use any library that simplifies your work;
- [ ] Host the API on the service of your choice;

# Endpoints
    
- [x] Get all activities:
- [x] Create activity
- [ ] Get cards by activityId
- [ ] Search cards by patientName, visitId or billId
- [ ] filter by PRIORITY, TO_RECEIVE or TO_SEND
- [ ] page: index of page
- [ ] perPage: number of elements in each page
- [ ] totalCardsOk: Number of cards (all pages) with slaStatus OK
- [ ] totalCardsWarning: Number of cards (all pages) with slaStatus WARNING
- [ ] totalCardsDelayed: Number of cards (all pages) with slaStatus DELAYED
- [ ] pageInfo: Add any new fields you think is important to build the pagination component in web page

- [x] Create card
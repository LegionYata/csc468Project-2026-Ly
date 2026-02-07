# The Visitor Counter
CSC 468 Project [Spring 2026]



```mermaid
graph LR
    User((Web Browser)) -- HTTP --> App[Python/Flask Web Server]
    App -- PyMongo/BSON --> DB[(MongoDB Instance)]
    DB -- Document Object --> App
    App -- View Count --> User
```

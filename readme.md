# Algorex 
### Trading App 



## Endpoints API

| Method | Route                    | Details                                                                                      |
|--------|--------------------------|----------------------------------------------------------------------------------------------|
| GET    | /api/login               | Login                                                                                        |
| POST   | /api/signup              | Signup                                                                                       |
| POST   | /api/wire                | Make a wire (deposit OR withdraw money)                                                      |
| GET    | /api/profile             | Fetch all the profile data, including the user's balance                                     |
| PATCH  | /api/update              | Update user's profile (except balance)                                                       |
| GET    | /api/trades/index        | Fetch all our trades                                                                         |
| GET    | /api/trades/index/open   | Fetch all our open trades                                                                    |
| GET    | /api/trades/index/closed | Fetch all our closed trades                                                                  |
| POST   | /api/openTrade/          | Open a long position (buy), the amount and the stock is specified in the body of the request |
| POST   | /api/closeTrade/:id      | Close the position                                                                           |
| GET    | /api/closedPNL           | Return the total closed PNL (all closed trades)                                              |
| GET    | /api/openPNL             | Return the total open PNL (all open trades)                                                  |
| GET    | /api/currentBalance      | Return current balance (all the money that is NOT in an open position)                       |

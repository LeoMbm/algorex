# Algorex 

### API For a Trading App





## Endpoints API

| Method | Route                     | Details                                                                                      |
|--------|---------------------------|----------------------------------------------------------------------------------------------|
| GET    | /api/login                | Login                                                                                        |
| POST   | /api/signup               | Signup                                                                                       |
| GET    | /api/profile              | Fetch all the profile data, including the user's balance                                     |
| PATCH  | /api/user                 | Update user's profile (except balance)                                                       |
| POST   | /api/trade/wire           | Make a wire (deposit OR withdraw money)                                                      |
| GET    | /api/trade/wire_index     | Fetch all the wire data (deposit and withdraw money)                                         |
| GET    | /api/trade/index          | Fetch all our trades                                                                         |
| GET    | /api/trade/index/open     | Fetch all our open trades                                                                    |
| GET    | /api/trade/index/closed   | Fetch all our closed trades                                                                  |
| POST   | /api/trade/openTrade/     | Open a long position (buy), the amount and the stock is specified in the body of the request |
| POST   | /api/trade/closeTrade/:id | Close the position                                                                           |
| GET    | /api/trade/closedPNL      | Return the total closed PNL (all closed trades)                                              |
| GET    | /api/trade/openPNL        | Return the total open PNL (all open trades)                                                  |
| GET    | /api/trade/currentBalance | Return current balance (all the money that is NOT in an open position)                       |

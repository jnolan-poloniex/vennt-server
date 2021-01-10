# vennt-server
A headless server for making API calls to the Vennt database.


### Running the server
`py -3 venntserver.py vennt.db`


# API Documentation
All communications with the server are done via JSON. Authentication is done via POST which gives you an `auth_token` that can be used to make GET calls.

### Create an account
POST: `{"register":"myusername","password":"mypassword"}`

Returns a JSON:
- `success`: whether the operation was successful
- `info`: on failure, why
- `auth_token`: on success, your authentication token for making GET calls

### Login
POST: `{"login":"myusername","password":"mypassword"}`

Returns a JSON:
- `success`: whether the operation was successful
- `info`: on failure, why
- `auth_token`: on success, your authentication token for making GET calls

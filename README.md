# builds-api

Authenticated Django REST Framework API for [Builds Frontend](https://github.com/t0ri/builds)


## Users
### Sign Up
`POST users/signup`

Expects key-value pairs
Returns 200 or 400 status
```
email:example@email.com
username:myusername
password:mypassword
```

### Sign In
`POST users/signin`

Expects key-value pairs
Returns auth token in JSON
```
username:myusername
password:mypassword
```


## Lots
### Get all lots belonging to user
`GET api/lots/user/<int:id>`
Expects User ID in URL
TODO: Get all lots belonging to User ID

### Get a lot
`GET api/lots/<int:id>`
Expects Lot ID in URL
TODO: Get the lot belonging to Lot ID

### Update existing build
`PUT api/lots/<int:id>/edit`
Expects Lot ID in URL, data from request object, user to be Lot author from request
TODO: Update a lot, given its ID and request data after validation if the request's user is the Lot author

### Delete existing lot
`DELETE api/lots/<id>/delete`
Expects Lot ID in URL, user to be Lot author from request
TODO: Delete the lot belonging to Lot ID if the request's user is the Lot author

### Post a new build
`POST api/lots/new`
Expects JSON, user ID
```
{
    "title": "My Title",
    "description": "My Description",
    "gallery": "http://www.my-link.com/",
    "lot_type": "str data from frontend UI", # UI picker
    "bedrooms": "2", # control from frontend for number only input
    "bathrooms": "1", # control from frontend for number only input
    "sims": "3", # control from frontend for number only input
    "packs": "["str", "array", "of", "packs"]" # CharField backend, handled in frontend
}
```
TODO: Save a new lot from request's serialized data

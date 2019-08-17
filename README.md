# builds-api
Authenticated Django REST Framework API for [Builds Frontend](https://github.com/t0ri/builds)

## Using the API
### Accounts
#### Sign Up
To create a profile, send a request to
`POST https://builds-gallery-api.herokuapp.com/users/signup`

##### Headers
`Content-Type:application/json`

##### Body
```
{
  "email": "myemail@email.com",
  "username": "myusername",
  "password": "mypassword"
}
```

### Sign In
To receive your auth token, send a request to
`POST https://builds-gallery-api.herokuapp.com/users/signin`

#### Headers
`Content-Type:application/json`

##### Body
```
{
  "username": "myusername",
  "password": "mypassword"
}
```


### Accessing Builds
#### Post a New Build
To post a new build, send a request to
`POST https://builds-gallery-api.herokuapp.com/api/lots/new`

##### Headers
```
Authorization:Token [token returned when signing in]
Content-Type:application/json
```

##### Body
```
{
    "name": "Lot Name",
    "description": "Lot Description.",
    "gallery": "Link the build's the EA Sims 4 Gallery post",
    "lot_type": "Residential",
    "bedrooms": "<int>",
    "bathrooms": "<int>",
    "sims": "<int>",
    "images": "link to already hosted image of build"
}
```

#### Delete Your Build
To delete your build, send a request to
`DELETE https://builds-gallery-api.herokuapp.com/api/lots/{lot_id}/delete`

##### Headers
`Authorization:Token [token returned when signing in]`

#### Update Your Build
To update your build, send a request to
`PATCH https://builds-gallery-api.herokuapp.com/api/lots/{lot_id}/edit`

##### Headers
`Authorization:Token [token returned when signing in]`

##### Body
Body should be fully filled out, including unchanged information.
```
{
    "name": "Updated Lot Name",
    "description": "Lot Description.",
    "gallery": "Link the build's the EA Sims 4 Gallery post",
    "lot_type": "Residential",
    "bedrooms": "<int>",
    "bathrooms": "<int>",
    "sims": "<int>",
    "images": "link to already hosted image of build"
}
```
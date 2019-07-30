# builds-api

Authenticated REST Django API for [Builds Frontend](https://github.com/t0ri/builds)


## Users
### Sign Up
`POST /users/signup`
Expects key-value pairs
```
email:example@email.com
username:myusername
password:mypassword
```

### Sign In
`POST /users/signin`
Expects key-value pairs
```
username:myusername
password:mypassword
```

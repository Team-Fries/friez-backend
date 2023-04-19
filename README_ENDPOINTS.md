## 🐌  https://is-it-raining.herokuapp.com/

- Base url for the API

___
### API ENDPOINT Shortcuts

| HTTP Verbs | Endpoints                          | Action                                     |
| ---------- | ---------------------------------- | ------------------------------------------ |
| GET        | /auth/users/                       | Return info for logged in user             |
| POST       | /auth/users/                       | Create new user                            |
| POST       | /auth/token/login/                 | User login                                 |
| POST       | /auth/token/logout/                | User logout                                |
| GET        | /auth/users/me/                    | Retreives authenticated user               |
| PATCH      | /auth/users/me/                    | Update authenticated user                  |
| DELETE     | /auth/users/me/                    | Delete authenticated user                  |


___

### Documentation
___

## 🐝   auth/users/

- Creates a new user if `POST` request, if `GET` request returns stored info for logged in user

- Allowed Request: GET, POST


Example POST:
```json
{
    "email": "bugsnacks@gmail.com",
	"username": "littlecowboy",
	"password": "toad4life"
}
```
Stored As:
```json
{
    "email": "bugsnacks@gmail.com",
    "id": 10,
    "username": "littlecowboy"
}
```
___

## 🌸   auth/token/login/

- User login (user gets token, expires after certain amount of time)

- Allowed Request: POST


Example POST:
```json
{
    "password": "quetzalcoatlus",
    "username": "ivar"
}
```

___

## 🐓   auth/token/logout/

- User logs out and token is destroyed

- Allowed Request: POST

___

## 🦆  auth/users/me/

- Retreives/updates/deletes the authenticated user

- Allowed Request: GET, PUT, PATCH, DELETE

___

### For more Djoser endpoints you can look here:
- `https://djoser.readthedocs.io/en/latest/base_endpoints.html#user`
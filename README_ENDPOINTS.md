## 🐌  https://is-it-raining.herokuapp.com/

- Base url for the API

___
### API ENDPOINT Shortcuts

| HTTP Verbs | Endpoints                             | Action                                     |
| ---------- | ------------------------------------  | ------------------------------------------ |
| GET        | /auth/users                           | Return info for logged in user             |
| POST       | /auth/users                           | Create new user                            |
| POST       | /auth/token/login                     | User login                                 |
| POST       | /auth/token/logout                    | User logout                                |
| GET        | /auth/users/me                        | Retreives authenticated user               |
| PATCH      | /auth/users/me                        | Update authenticated user                  |
| DELETE     | /auth/users/me                        | Delete authenticated user                  |
| GET        | /weather-animal/\<int:original_code\> | Random animal for weather passed in        |
| GET        | /list-animals                         | List of all animals                        |

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

## 🦈   weather-animal/\<int:original_code\>

- Randomly chooses an animal of the weather type passed in, `original_code` is the code for each weather type from the API documentation (ex. 800 for Clear, 100 for Thunderstorm)

- Allowed Request: GET


Stored As:
```json
{
	"id": 10,
	"name": "Toucan",
	"weather": 9,
	"image": null
}
```
___

## 🐆   list-animals/

- List out all animals in the database

- Allowed Request: GET


Stored As:
```json
	{
		"id": 7,
		"name": "Megalodon",
		"weather": 6,
		"image": null
	},
	{
		"id": 8,
		"name": "Goat",
		"weather": 7,
		"image": null
	},
	{
		"id": 9,
		"name": "Trex",
		"weather": 8,
		"image": null
	}
```
___



### For more Djoser endpoints you can look here:
- `https://djoser.readthedocs.io/en/latest/base_endpoints.html#user`
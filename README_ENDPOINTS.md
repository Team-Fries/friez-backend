## 🐌  https://is-it-raining.herokuapp.com/

- Base url for the API

___
### API ENDPOINT Shortcuts

| HTTP Verbs | Endpoints                                                               | Action                                     |
| ---------- | ----------------------------------------------------- | ------------------------------------------ |
| GET        | /auth/users                                           | Return info for logged in user             |
| POST       | /auth/users                                           | Create new user                            |
| POST       | /auth/token/login                                     | User login                                 |
| POST       | /auth/token/logout                                    | User logout                                |
| GET        | /auth/users/me                                        | Retreives authenticated user               |
| PATCH      | /auth/users/me                                        | Update authenticated user                  |
| DELETE     | /auth/users/me                                        | Delete authenticated user                  |
| GET        | /weather-animal/\<int:original_code\>                 | Random animal for weather passed in        |
| GET        | /animal-detail/\<str:name\>                           | Details for single animal                  |
| GET        | /list-animals                                         | List of all animals in database            |
| POST       | /captured/\<str:name\>                                | Captures animal passed in                  |
| DELETE     | /captured/\<str:name\>                                | Remove animal passed in                    |
| GET        | /my-animals                           		         | List all the user's caught animals         |
| POST       | /trade                                                | User sends a request to trade              |
| GET        | /my-offers                                            | List offers logged in user has created     |
| GET        | /my-received-offers                                   | List offers recieved from other users      |

🦣 🐁 🐸 🐄 🐴 🐈 🐕 🦏 🐘 🐇 🦃 🦜 🐍 🐋 🐞 🕷️ 🪲 🦂 🦒 🐏 🦌 🐜 🐖 🐐 🦦 🦉 🦎 🐟 🐔 🦬 🐬 🐥 🐙 🪰 🐛 🦤 🦨 

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

## 🐠   auth/token/login/

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

## 🦈   weather-animal/\<int:original_code\>/

- Randomly chooses an animal of the weather type passed in 

- `<int:original_code>` is replaced with the code for weather type from the API documentation - (ex. 800 for Clear, 100 for Thunderstorm)

- Allowed Request: GET


Stored As:
```json
{
	"id": 10,
	"name": "Toucan",
	"image": null,
	"weather": "Clear"
}
```
___

## 🐺   animal-detail/\<str:name\>/

- View details about single animal

- `<str:name>` is replaced with animal name

- Allowed Request: GET


Stored As:
```json
{
	"id": 7,
	"name": "Megalodon",
	"image": null,
	"weather": "Rain"
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
		"image": null,
		"weather": "Rain"
	},
	{
		"id": 8,
		"name": "Goat",
		"image": null,
		"weather": "Snow"
	},
	{
		"id": 9,
		"name": "Trex",
		"image": null,
		"weather": "Atmosphere"
	}
```
___

## 🐊   captured/\<str:name\>/

- If `POST` request, the logged in user captures the animal who's name is passed in (can be upper or lower case)

- If `DELETE` request, the logged in user releases the animal passed in

- `<str:name>` is replaced with animal's name

- Allowed Request: POST, DELETE


Stored As:
```json
{
	"owner": "ivar",
	"animal": "Trex"
}
```
___

## 🦋   my-animals/

- List out all the animals the logged in user has caught

- Allowed Request: GET


Stored As:
```json
[
	{
		"owner": "ivar",
		"animal": "Trex"
	},
	{
		"owner": "ivar",
		"animal": "Stegosaurus"
	},
	{
		"owner": "ivar",
		"animal": "Toucan"
	},
	{
		"owner": "ivar",
		"animal": "Goat"
	},
	{
		"owner": "ivar",
		"animal": "Alligator"
	}
]
```
___

## 🦇   trade/

- Logged in user makes a request to another user to trade animals

- Allowed Request: POST



Expects these fields in POST request:
```json
{
	"trade_receiver": "superuser",
	"offered_animal": "Stegosaurus",
	"desired_animal": "Megalodon"
}
```

Stored As:
```json
{
	"id": 4,
	"trade_starter": "ivar",
	"trade_receiver": "superuser",
	"offered_animal": {
		"owner": "ivar",
		"animal": {
			"id": 11,
			"name": "Stegosaurus",
			"weather": "Clouds",
			"images": [],
			"random_image": null
		}
	},
	"desired_animal": {
		"owner": "superuser",
		"animal": {
			"id": 7,
			"name": "Megalodon",
			"weather": "Rain",
			"images": [],
			"random_image": null
		}
	}
}
```
___

## 🪱   my-offers/

- List of all the offers the logged in user has created

- Allowed Request: GET

___

## 🐢   my-received-offers/

- List of all the offers logged in user has received from other users

- Allowed Request: GET

___

##   


### For more Djoser endpoints you can look here:
- `https://djoser.readthedocs.io/en/latest/base_endpoints.html#user`
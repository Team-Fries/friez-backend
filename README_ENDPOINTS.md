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
| GET        | /auth/users/me                                        | Retrieve authenticated user                |
| PATCH      | /auth/users/me                                        | Update authenticated user                  |
| DELETE     | /auth/users/me                                        | Delete authenticated user                  |
| GET        | /weather-animal/\<int:original_code\>                 | Random animal for weather passed in        |
| GET        | /animal-detail/\<str:name\>/\<str:variation_type\>    | Details for single animal                  |
| GET        | /list-animals                                         | List of all animals in database            |
| POST       | /captured/\<str:name\>/\<str:variation\>              | Captures animal passed in                  |
| DELETE     | /captured/\<str:name\>/\<str:variation\>              | Remove animal passed in                    |
| GET        | /my-animals                           		         | List all the user's caught animals         |
| GET        | /my-special-animals                           		 | List all Special animals                   |
| POST       | /trade                                                | User sends a request to trade              |
| GET        | /my-offers                                            | List offers logged in user created         |
| GET        | /my-received-offers                                   | List offers recieved from other users      |
| POST       | /trade/accept/\<int:trade_id\>                        | Accept a trade                             |
| GET        | /background/                                          | Retrieve Background Image                  |
     


🦣 🐁 🐸 🐄 🐴 🐈 🐕 🦏 🦤 🐘 🐇 🦃 🐍 🐋 🕷️ 🪲 🦂 🦒 🐏 🦌 🐜 🐖 🐐 🦦 🦉 🦎 🐟 🐔 🦬 🐬 🐥 🐙 🪰 🐛 🦨 

### Documentation
___

## 🐝   auth/users/

- Creates a new user if POST request, if GET request returns stored info for logged in user

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
	"id": 15,
	"name": "Toucan",
	"weather": "Clear",
	"variation_type": "B",
	"image": "https://team-fries-images.s3.amazonaws.com/team-fries-images/toucan_yellow_by_cleopatrawolf_dfv0vap_WVfFXCp.gif",
	"can_capture": true,
	"points_left_until_max": 10
}
```
___

## 🐺   animal-detail/\<str:name\>/\<str:variation_type\>/

- View details about single animal

- `<str:name>` is replaced with animal name

- `<str:variation_type>` is replaced with animal variation

- Allowed Request: GET


Stored As:
```json
{
	"id": 9,
	"name": "Trex",
	"weather": "Atmosphere",
	"variation_type": "A",
	"image": "https://team-fries-images.s3.amazonaws.com/team-fries-images/trex_brown_by_cleopatrawolf_dfv0vae_LInp5lw.gif",
	"can_capture": false,
	"points_left_until_max": 7
}
```
___

## 🐆   list-animals/

- List out all animals in the database

- Allowed Request: GET


Stored As:
```json
{
	"id": 12,
	"name": "Quetzalcoatlus",
	"weather": "Clear",
	"variation_type": "A",
	"image": "https://team-fries-images.s3.amazonaws.com/team-fries-images/quetzalcoatlus_black_by_cleopatrawolf_dfv8lke_74KRo7V.gif",
	"can_capture": false,
	"points_left_until_max": 0
},
{
	"id": 5,
	"name": "Alligator",
	"weather": "Thunderstorm",
	"variation_type": "A",
	"image": "https://team-fries-images.s3.amazonaws.com/team-fries-images/alligator_green_by_cleopatrawolf_dfv8lhg_83XWY4I.gif",
	"can_capture": true,
	"points_left_until_max": 10
},
```
___

## 🦜   my-special-animals/

- List of all the user's Special Animals

- Allowed Request: GET


Stored As:
```json
{
	"id": 13,
	"owner": "ivar",
	"image": null,
	"animal_name": "Quetzalcoatlus",
	"variation_type": "A"
},
{
	"id": 14,
	"owner": "ivar",
	"image": null,
	"animal_name": "Trex",
	"variation_type": "A"
}

```

## 🐊   captured/\<str:name\>/\<str:variation\>/ 

- If POST request, the logged in user captures the animal who's name is passed in (can be upper or lower case)

- If DELETE request, the logged in user releases the animal passed in

- `<str:name>` is replaced with animal's name

- `<str:variation>` is replaced with animal's variation

- Allowed Request: POST, DELETE


Stored As:
```json
{
	"owner": "ivar",
	"animal": {
		"id": 17,
		"name": "Trex",
		"weather": "Atmosphere",
		"variation_type": "B",
		"image": null,
		"can_capture": false
	},
	"points": 4
}
```
___

## 🦋   my-animals/

- List out all the animals the logged in user has caught

- Allowed Request: GET


Stored As:
```json
	{
		"owner": "ivar",
		"animal": {
			"id": 10,
			"name": "Toucan",
			"weather": "Clear",
			"variation_type": "A",
			"image": "https://team-fries-images.s3.amazonaws.com/team-fries-images/toucan_black_by_cleopatrawolf_dfv0vav_NSlUIpJ.gif",
			"can_capture": true
		},
		"points": 2
	},
	{
		"owner": "ivar",
		"animal": {
			"id": 16,
			"name": "Alligator",
			"weather": "Thunderstorm",
			"variation_type": "B",
			"image": null,
			"can_capture": true
		},
		"points": 0
	},
	{
		"owner": "ivar",
		"animal": {
			"id": 15,
			"name": "Toucan",
			"weather": "Clear",
			"variation_type": "B",
			"image": "https://team-fries-images.s3.amazonaws.com/team-fries-images/toucan_yellow_by_cleopatrawolf_dfv0vap_WVfFXCp.gif",
			"can_capture": true
		},
		"points": 9
	},
```
___

## 🦇   trade/

- Logged in user makes a request to another user to trade animals

- Allowed Request: POST

- Expects POST request with a payload with the required fields: `'trade_receiver', 'offered_animal', 'desired_animal'`


Example:
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
	"id": 3,
	"trade_starter": "ivar",
	"trade_receiver": "superuser",
	"status": "pending",
	"offered_animal": "Toucan",
	"desired_animal": "Toad"
},
{
	"id": 4,
	"trade_starter": "ivar",
	"trade_receiver": "superuser",
	"status": "accepted",
	"offered_animal": "Stegosaurus",
	"desired_animal": "Megalodon"
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

## 🐞   trade/accept/\<int:trade_id\>/

- Accept trade offer and animals will swap animals

- Only trade_receiver can accept, NOT the person who started the trade (will say: 'You are not authorized to accept this trade request.')

- replace `<int:trade_id>` with trade id

- Allowed Request: POST

___

## 🐞   background/

- Display correct background image per weather condition and day or night

- Allowed Rquest: GET

- ** URL needs query parameters after 'background/': 'code,' for the 3-digit weather code, and 'timeofday' which needs to be 'am' or 'pm' (example below)

Example URL:
```
https://is-it-raining.herokuapp.com/background/?code=800&timeofday=am
```

___

### For more Djoser endpoints you can look here:
- `https://djoser.readthedocs.io/en/latest/base_endpoints.html#user`
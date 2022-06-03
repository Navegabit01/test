
# Test new Jobs

This project is thinked for testing real skill of development in (CRUD + Database + API + Security + Testing)


## Authors

- [@Navegabit01](https://github.com/Navegabit01)


## Installation

Install my project with pip

```bash
  pip3 install -r requirements.txt
  python manange.py runserver
```

Populate Database 
```bash
  python manage.py seed_profile --profiles_total #{amount_of_profiles} >= 2
```    
## Acknowledgements

 - [Rest-Framework documentation](https://www.django-rest-framework.org/)
 - [RandomAPI](https://randomapi.com/documentation)
## API Reference


#### Post Profile

```http
  POST friends/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `profile1`             | `integer`  | **Required**. Profile 1   |
| `profile2`             | `integer`  | **Required**. Profile 2   |

#### Get Profile items

```http
  GET profile/
```

#### Get item

```http
  GET profile/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Post Profile

```http
  POST profile/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `img`             | `File`    | Image of profile           |
| `first_name`      | `string`  | **Required**. First name   |
| `last_name`       | `string`  | **Required**. Last name    |
| `phone`           | `string`  | **Required**. Phone        |
| `address`         | `string`  | **Required**. Address      |
| `city`            | `string`  | **Required**. City         |
| `zipcode`         | `integer` | Zipcode                    |
| `available`       | `string`  | Available                  |

#### Get Friends items

```http
  GET friends/
```

#### Get Item

```http
  GET friends/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Get Profile known friends

```http
  GET friends/profile/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of profile |

#### Get Profile shortest path

```http
  GET friends/profile/${id_1}/${id_2}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id_1`      | `string` | **Required**. Id of profile |
| `id_2`      | `string` | **Required**. Id of profile |
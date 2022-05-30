
# Test Backend API 

This is a simulations of relations in profiles 


## Authors

- [@Navegabit01](https://github.com/Navegabit01)


## Installation

Install my-project with pip

```bash
  pip install -r requirements.txt
```
    
## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## API Reference

#### Get all Profiles

```http
  GET /profiles/
```

#### Get profile

```http
  GET /profiles/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |



# 0x06. Star Wars API

```
## Description

The Star Wars API (SWAPI) is a RESTful web service that provides data from the Star Wars universe, including information about characters, planets, starships, vehicles, species, and films. This API is an invaluable resource for developers, enthusiasts, and fans who want to explore and interact with Star Wars data programmatically.

## Features

- Retrieve detailed information about various entities from the Star Wars universe.
- Search for specific characters, planets, starships, vehicles, species, or films.
- Access comprehensive data including names, attributes, and relationships between entities.
- Cross-referencing data to explore connections within the Star Wars universe.

## Endpoints
The SWAPI offers several endpoints to access different types of data:

- `/people`: Retrieve information about characters in the Star Wars universe.
- `/planets`: Retrieve information about planets featured in the Star Wars films.
- `/starships`: Retrieve information about starships used in the Star Wars universe.
- `/vehicles`: Retrieve information about vehicles featured in the Star Wars films.
- `/species`: Retrieve information about species in the Star Wars universe.
- `/films`: Retrieve information about films in the Star Wars saga.

For detailed documentation on each endpoint and available query parameters, refer to the [SWAPI documentation](https://swapi.dev/documentation).

## Usage
To use the Star Wars API, send HTTP requests to the appropriate endpoint, specifying any required parameters. The API will respond with JSON-formatted data containing the requested information.

Example:
```
GET https://swapi.dev/api/people/1
```

Response:
```json
{
    "name": "Luke Skywalker",
    "height": "172",
    "mass": "77",
    "hair_color": "blond",
    "skin_color": "fair",
    "eye_color": "blue",
    "birth_year": "19BBY",
    "gender": "male",
    "homeworld": "https://swapi.dev/api/planets/1/",
    ...
}
```

## Getting Started

To get started with the Star Wars API, follow these steps:
1. Make HTTP requests to the desired endpoint using your preferred programming language or HTTP client.
2. Parse the JSON response to extract the information you need.
3. Explore the various endpoints and entities available in the API to retrieve specific data.

## Credits
The Star Wars API (SWAPI) is maintained by the SWAPI development team and contributors. For more information and updates, visit the [official SWAPI website](https://swapi.dev/).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

# Anchor API

## Introduction
Anchor API is a FastAPI application designed for creating and managing symlinks for multimedia files. It automates the renaming and organization of movie and TV show files based on metadata from MDBList, ideal for media libraries like Plex.

## Features
- Fetch movie and TV show metadata from MDBList using IMDb IDs.
- Create symlinks with customizable naming schemes.
- Support for both movies and TV series.

## Prerequisites
- Docker
- Docker Compose
- Python 3.8 or higher

## Installation
1. Clone the repository & cd into the directory

2. Set your MDB API key in the docker-compose-example.yml:
   ```yml
   MDB_API_KEY=your_mdb_api_key
   ```

3. Rename docker-compose-example.yml to docker-compose.yml

4. Build and run the Docker container:
   ```bash
   docker-compose up -d
   ```

## Usage

### Create a Movie Symlink (cURL)
```bash
curl -X POST http://localhost:8000/symlink/movie \
-H "Content-Type: application/json" \
-d '{"filename":"movie-file.mp4", "imdb_id":"tt0111161", "library_name":"Movies"}'
```

### Create a TV Series Symlink (cURL)
```bash
curl -X POST http://localhost:8000/symlink/series \
-H "Content-Type: application/json" \
-d '{"filename":"series-folder", "imdb_id":"tt0944947", "library_name":"TV Shows"}'
```

## Developer Integration

### Create a Movie Symlink (Python)
```python
import requests

data = {
    "filename": "movie-file.mp4",
    "imdb_id": "tt0111161",
    "library_name": "Movies"
}

response = requests.post("http://localhost:8000/symlink/movie", json=data)
print(response.json())
```

### Create a TV Series Symlink (Golang)
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
)

func main() {
	data := map[string]string{
		"filename":     "series-folder",
		"imdb_id":      "tt0944947",
		"library_name": "TV Shows",
	}
	jsonData, err := json.Marshal(data)
	if err != nil {
		panic(err)
	}

	resp, err := http.Post("http://localhost:8000/symlink/series", "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	fmt.Println("Response status:", resp.Status)
}
```

## Contributing
Contributions are welcome! Feel free to submit pull requests, create issues, or suggest new features.

## License
This project is licensed under [MIT License](LICENSE).

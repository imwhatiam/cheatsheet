# elasticsearch

## create index

```
curl -XPUT "http://localhost:9200/movies/movie/1" -d'
{
    "title": "The Godfather",
    "director": "Francis Ford Coppola",
    "year": 1972,
    "genres": ["Crime", "Drama"]
}' -H 'Content-Type: application/json'

curl -XPUT "http://localhost:9200/movies/movie/2" -d'
{
    "title": "Lawrence of Arabia",
    "director": "David Lean",
    "year": 1962,
    "genres": ["Adventure", "Biography", "Drama"]
}' -H 'Content-Type: application/json'

curl -XPUT "http://localhost:9200/movies/movie/3" -d'
{
    "title": "To Kill a Mockingbird",
    "director": "Robert Mulligan",
    "year": 1962,
    "genres": ["Crime", "Drama", "Mystery"]
}' -H 'Content-Type: application/json'

curl -XPUT "http://localhost:9200/movies/movie/4" -d'
{
    "title": "Apocalypse Now",
    "director": "Francis Ford Coppola",
    "year": 1979,
    "genres": ["Drama", "War"]
}' -H 'Content-Type: application/json'

curl -XPUT "http://localhost:9200/movies/movie/5" -d'
{
    "title": "Kill Bill: Vol. 1",
    "director": "Quentin Tarantino",
    "year": 2003,
    "genres": ["Action", "Crime", "Thriller"]
}' -H 'Content-Type: application/json'

curl -XPUT "http://localhost:9200/movies/movie/6" -d'
{
    "title": "The Assassination of Jesse James by the Coward Robert Ford",
    "director": "Andrew Dominik",
    "year": 2007,
    "genres": ["Biography", "Crime", "Drama"]
}' -H 'Content-Type: application/json'
```

## search

```
curl -XPOST "http://localhost:9200/_search" -d'
{
    "query": {
        "query_string": {
            "query": "ford",
            "fields": ["title"]
        }
    }
}' -H 'Content-Type: application/json'
```

```
{
    "took": 561,
    "timed_out": false,
    "_shards": {
        "total": 4,
        "successful": 4,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 2,
            "relation": "eq"
        },
        "max_score": 1.0467482,
        "hits": [
            {
                "_index": "movies",
                "_type": "movie",
                "_id": "3",
                "_score": 1.0467482,
                "_source": {
                    "title": "To Kill a Mockingbird",
                    "director": "Robert Mulligan",
                    "year": 1962,
                    "genres": [
                        "Crime",
                        "Drama",
                        "Mystery"
                    ]
                }
            },
            {
                "_index": "movies",
                "_type": "movie",
                "_id": "5",
                "_score": 1.0467482,
                "_source": {
                    "title": "Kill Bill: Vol. 1",
                    "director": "Quentin Tarantino",
                    "year": 2003,
                    "genres": [
                        "Action",
                        "Crime",
                        "Thriller"
                    ]
                }
            }
        ]
    }
}
```

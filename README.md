WikiPages
=========


<a href="https://github.com/vchaptsev/cookiecutter-django-vue">
    <img src="https://img.shields.io/badge/Based%20on-Cookiecutter%20Django%20Vue-blue.svg" />
</a>



### Development

+ edit `.env`
+ run `docker-compose up --build`
+ open `0.0.0.0:8000`  (**important:** for Cross-Origin Resource Sharing (CORS) )

![](wikipages.gif)


### GraphQL example

`http://0.0.0.0:8000/api-graphql/`

```graphql
query ($title: String)
{
  wikipage(title: $title) {
    title
    author {
      email
    }
  }
  user(id: 4) {
    email
  }
  allUsers {
    id
    wikipages {
      title
    }
  }
  allWikipages {
    id
    }
}

```

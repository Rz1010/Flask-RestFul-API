# Machine Learning Engineer technical challenge

## Task

### Coding

Add or update modules, methods, snippets or files in order to implement a RESTful API providing the below functionalities:

- Photo API: extract human face(s) locations, if any, from an image
- Audio API: extract non-silent chunks from an audio file
- Text API: extract named entities (English) from a text file

_Endpoints paths, input and output formats are a free choice._

You can add any external dependency unless it is a wrapper for, or it uses, an online service. Solution is meant to work on premises
and thus, will be tested in an offline environment.

### Packaging

Write and use the _Dockerfile_ to ship this to production.

Product should serve functionalities as APIs using a production application server, and to be proxied using a web
server ([nginx](conf/challenge.nginx)).

## Submission

Your solution should consist of both project repository and Docker image.

_Sharing any piece of information on Gitlab outside the private project forked from challenge repository will not be
considered and could lead to user ban._

### Duration

Solution must be submitted in less than **3 days** after your first login to Gitlab.

### Repository

- Fork this repository to a private personal project
- Add [Administrator](https://gitlab.intaliojobs.ml/root) user to project members as
  a [Maintainer](https://docs.gitlab.com/ee/user/project/members/#add-groups-to-a-project)
- Changes should be pushed to your project on **main** branch.
- Archive the repository once coding part is done

### Docker image

Docker image to be pushed to
[Gitlab Container Registry](https://docs.gitlab.com/ee/user/packages/container_registry/)
of your own fork from challenge repository.

## Bonus

Extra points can be earned from doing any of the below:

- Extending Photo API to support PDF input
- Extending Audio API to return chunks timings (start/end)
- Extending Text API to support Arabic text
- Implementing unit and API tests in [test directory](tests)
- Not putting source code inside Docker image
- Automating [Docker builds](https://docs.gitlab.com/ee/ci/docker/using_docker_build.html)

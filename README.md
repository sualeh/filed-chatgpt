# filed-chatgpt


## Use Docker Image

Run a command similar to the one below, after substituting your OpenAI API key:

```sh
docker run \
--mount type=bind,source="${PWD}",target=/opt/filed_chatgpt/share \
--rm -it \
--env OPENAI_API_KEY=your_openai_api_key \
sualehfatehi/filed_chatgpt \
-o share/out.yaml
```

## Build Docker Image

To build the Docker image locally, run:

```sh
docker build -t filed_chatgpt .
docker image tag filed_chatgpt sualehfatehi/filed_chatgpt:latest
```

## to setup
poetry install


## to start server
poetry run devß

## To end process
pkill -9 Python

## Reference to add my own plugin
```
langchain.tools import AIPluginTool
tool = AIPluginTool.from_plugin_url('')
```

https://towardsdatascience.com/the-easiest-way-to-interact-with-language-models-4da158cfb5c5
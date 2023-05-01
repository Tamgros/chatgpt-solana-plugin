## to setup
poetry install


## to start server
poetry run dev

## To end process
ps -ef|grep python
or
sudo lsof -i:333


pkill -9 <pid>
kill -9 <pid>

## Reference to add my own plugin
```
langchain.tools import AIPluginTool
tool = AIPluginTool.from_plugin_url('')
```

https://towardsdatascience.com/the-easiest-way-to-interact-with-language-models-4da158cfb5c5

## Noah's JS implementation
https://github.com/ngundotra/solana-gpt-plugin

## Got approved!
plugin link
https://chat.openai.com/?model=text-davinci-002-plugins

## Python examples
https://chainstack.com/solana-python-tutorial-for-stepn/
https://github.com/solana-labs/chatgpt-plugin/blob/master/langchain_examples/python/main.py

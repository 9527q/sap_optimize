# 格式化

```shell
F=$(git status -s | grep -E '(\.py)|(/)$' | cut -c 4-); isort `echo $F`; black `echo $F`; flake8 `echo $F`; unset F
```

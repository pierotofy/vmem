# vmem

Cross-platform drop-in replacement for [psutil](https://github.com/giampaolo/psutil)'s virtual_memory function, without native extensions, Cygwin compatible.

## Install

`pip install -U vmem`

## Usage

```
>>> from vmem import virtual_memory
>>> virtual_memory()
svmem(total=68658819072, available=34382245888, percent=49.9, used=34276573184, free=34382245888)
```

## License

GPLv3
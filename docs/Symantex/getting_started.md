---
title: Getting Started
description: Getting started with Symantex
slug: /projects/symantex/getting-started/
sidebar_position: 1
---

-----------------------------------------

# Getting Started

## 1  Install

```bash
pip install symantex            # will download from PyPI
```

## 2  Set your API key

Symantex uses OpenAI under the hood, so ensure that you have an OpenAI key.

More providers will come soon...

```bash
export SYMANTEX_KEY="sk‑..."   # bash/zsh
```

## 3  Hello, Symantex!

```python
from symantex.core import Symantex
import os

sx = Symantex()
sx.register_key(os.environ["SYMANTEX_KEY"])
exprs, multiple = sx.to_sympy(r"x^2 + y^2 = 1")
print(exprs)          # → [Eq(Add(Pow(x, 2), Pow(y, 2)), 1)]
print(multiple)       # → False
```

*That’s it.*  Keep reading **Usage** for more nuanced examples.


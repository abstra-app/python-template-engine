# Python template

This is a super simple template engine for rendering HTML using python interpolation

```html
<python>
name = "World"
</python>

<h1>Hello { name }</h1>
```

# How to use

To see the generated code
```bash
python src/main.py examples/hello.html
```

To see the rendered output
```bash
python src/main.py examples/hello.html print | python
```

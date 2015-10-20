# jinja2 templates

## control statements

```
{% if title %}

{% else %}

{% endif %}
```

## loops

```
{% for post in posts %}
{% endfor %}
```

## Template Inheritance

```
{% extends "base.html" %}
{% block content %}
....
{% endblock %}
```

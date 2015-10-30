# client-side translate

- add a language field in Post model
- detect the language of each post when submitted
- display the "translate" link

## guess_language

the `guess_language` has some issues with python3, so use a fork.

```
sk/bin/pip uninstall guess-language
flask/bin/pip install https://bitbucket.org/spirit/guess_language/downloads/guess_language-spirit-0.5a4.tar.bz2
```

## translation services

- google
- microsoft

## calling microsoft translate api

[stackoverflow](http://stackoverflow.com/questions/24069197/httpresponse-object-json-object-must-be-str-not-bytes)

remember to decode utf-8

## ajax call

### server side

translate view function, accept 'POST' request

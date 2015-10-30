# debug, test and performance

## delete bug

Usually when multi-threaded, different session try to add the same object
to different sessions at the same time.

## Regression Testting

The best option every time a bug is discovered is to create a unit test for it, so that we can make sure we don't have a regression in the future.

## Test Coverage

`coverage`

```python
from coverage import coverage
cov = coverage(branch=True, omit=['flask/*', 'tests.py'])
cov.start()
```

```python
if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass
    cov.stop()
    cov.save()
    print "\n\nCoverage Report:\n"
    cov.report()
    print "\nHTML version: " + os.path.join(basedir, "tmp/coverage/index.html")
    cov.html_report(directory='tmp/coverage')
    cov.erase()
```

We have to catch and pass exceptions from the unit testing framework, because if not the script would end without giving us a chance to produce a coverage report.

## Profiling for performance

`profiling`, python comes with a nice source code profiler called `cProfile`.

## Database Performance

1. in `config.py`

`SQLALCHEMY_RECORD_QUERIES = True`

2. add a hook after each request

# Contributing

## Running the tests

There is no automated test suite yet. Until one exists, verify changes by
running these checks from the repository root.

Check the shell script prints a date and directory:

```sh
./hello.sh
```

Check the static server serves the repo at <http://localhost:8000>:

```sh
npm start
```

When adding a test framework, wire it up as `npm test` and replace the above.

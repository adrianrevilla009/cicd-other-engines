# teamcity-circleci-awareness

The same Maven job written as a TeamCity Kotlin DSL (`.teamcity/settings.kts`) and as a CircleCI config (`.circleci/config.yml`).

## Goal

Give a short, side-by-side feel for two more engines: TeamCity configures builds as code in Kotlin, CircleCI uses YAML with Docker images.

## Run it

```
python3 validate.py
```

Expected output: `teamcity-circleci-awareness OK`.

Not run end to end: it needs a TeamCity server and a CircleCI project. The Kotlin file is never compiled; `validate.py` reads it with a regular expression and parses the CircleCI YAML.

## What it proves

- CircleCI: the job `build-test-package` uses the image `cimg/openjdk:21.0`, runs three `mvn` commands after `checkout`, and calls `store_test_results` on `target/surefire-reports`.
- TeamCity: the build type `Build` has three Maven steps with goals `compile`, `verify` and `-DskipTests package`, under DSL version `2024.12`.
- Both configs hold the same three goals in the same order, which `validate.py` checks.

## Trade-offs

- Both files use a single job with sequential steps, so there are no separate stages or artifact publishing.
- The Kotlin DSL gives type checking in an IDE, but needs a TeamCity server to be used, and the check here is textual only.
- CircleCI's image tag is `21.0`, a moving tag, so builds can change without a commit.

## When not to use it

- If you must evaluate either engine seriously, build a real project on it; this folder only shows the config shape.
- For a team already standardised on another engine, adding a third tool is rarely worth it.

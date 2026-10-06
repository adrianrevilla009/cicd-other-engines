# gitlab-ci

A `.gitlab-ci.yml` that builds, tests and packages the Orders service in three stages, plus a script that checks its shape offline.

## Goal

Show the build, test, package pipeline in GitLab CI syntax, including caching and test reports. This is the reference shape the other folders repeat.

## Run it

```
python3 validate.py
```

Expected output: `gitlab-ci OK`.

Not run end to end: the pipeline was never executed on a GitLab runner. `validate.py` only parses the YAML and asserts the structure.

## What it proves

- `stages` is exactly `build`, `test`, `package`, and each stage has at least one job (checked by `validate.py`).
- The `test` job runs `mvn -B -ntp verify` and publishes `target/surefire-reports/*.xml` as a JUnit report with `when: always`, so failures still show up.
- The `package` job has a `rules` entry that limits it to `$CI_DEFAULT_BRANCH` and keeps `target/*.jar` as an artifact.
- The Maven repository is moved to `.m2/` inside the project and cached under the key `maven`.

## Trade-offs

- The cache key is a constant, so a changed `pom.xml` does not invalidate it.
- The `build` stage compiles and `test` runs `verify` again, which repeats work. This keeps the stages visible and is the same in every folder.
- `validate.py` cannot catch GitLab-specific errors such as bad `rules` expressions; only a lint in GitLab or a real run does.

## When not to use it

- If you need the real answer on whether a config is valid, use GitLab's own CI lint instead of this structural check.
- For a single short job, three stages add overhead without benefit.

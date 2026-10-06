# azure-devops-pipelines

An `azure-pipelines.yml` with three stages (build, test, package) for the Orders service, plus an offline structure check.

## Goal

Show the build, test, package pipeline in Azure DevOps syntax: stages with `dependsOn`, test result publishing and a published artifact.

## Run it

```
python3 validate.py
```

Expected output: `azure-devops-pipelines OK`.

Not run end to end: it was never executed in an Azure DevOps organisation. `validate.py` only parses the YAML and asserts the structure.

## What it proves

- The stages are `build`, `test`, `package`; `test` has `dependsOn: build` and `package` has `dependsOn: test`, and each stage has jobs.
- The pipeline triggers on `main` and runs on the `ubuntu-24.04` hosted image.
- `PublishTestResults@2` runs with `condition: always()` on `target/surefire-reports/*.xml`, so results appear even when tests fail.
- The package stage publishes `target` as the artifact `orders-jar`.

## Trade-offs

- The steps call `mvn` directly and rely on the hosted image having Maven; the version is not pinned in this file.
- `PublishTestResults@2` has no `testResultsFormat`, so it uses the task default (JUnit).
- Publishing the whole `target` directory is simple, but ships more than the jar.

## When not to use it

- If your code and reviews live elsewhere and you do not use Azure Boards or Azure Artifacts, another engine avoids an extra system.
- For a one-job build, stages are more structure than needed.

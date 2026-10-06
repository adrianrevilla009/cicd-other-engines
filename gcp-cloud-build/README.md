# gcp-cloud-build

A `cloudbuild.yaml` with three Maven steps (build, test, package) ordered by `waitFor`, plus an offline structure check.

## Goal

Show the build, test, package flow on Google Cloud Build, where every step is a container and order is set explicitly.

## Run it

```
python3 validate.py
```

Expected output: `gcp-cloud-build OK`.

Not run end to end: it needs a Google Cloud project with Cloud Build enabled. Nothing was submitted. `validate.py` only parses the YAML and asserts the structure.

## What it proves

- The steps have ids `build`, `test`, `package`, each running `mvn` from `maven:3.9.9-eclipse-temurin-21`.
- Each step after the first has `waitFor` naming the one before; `validate.py` asserts that chain.
- `target/*.jar` is uploaded to a Cloud Storage location under `gs://placeholder-bucket/orders`, a dummy bucket name that must be replaced.
- Logs go to Cloud Logging only (`CLOUD_LOGGING_ONLY`) and the build times out after `600s`.

## Trade-offs

- All steps share the `/workspace` directory automatically, which is convenient but means steps are not isolated.
- Without Maven caching, every run downloads dependencies again.
- There is no JUnit report feature as in GitLab or Azure; test results are only in the logs.

## When not to use it

- If your workloads and registry are not on Google Cloud, the storage and logging integrations do not help.
- For builds needing long caches or many parallel jobs, check quotas and build time costs first.

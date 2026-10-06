# cicd-other-engines

The same Maven pipeline (compile, verify, package) for an Orders service written for seven CI/CD engines, each with an offline script that checks its structure.

## What is inside

| Folder | What it shows | Run |
|---|---|---|
| `gitlab-ci/` | Stages, cache, JUnit report and a default-branch-only package job | `python3 gitlab-ci/validate.py` |
| `tekton/` | One reusable `Task` and a `Pipeline` chained with `runAfter` | `python3 tekton/validate.py` |
| `argo-workflows/` | A DAG `Workflow` with one parameterised container template | `python3 argo-workflows/validate.py` |
| `azure-devops-pipelines/` | Three stages linked with `dependsOn`, test results and artifact publishing | `python3 azure-devops-pipelines/validate.py` |
| `aws-codepipeline-codebuild/` | A CodeBuild `buildspec.yml` plus a CodePipeline definition in JSON | `python3 aws-codepipeline-codebuild/validate.py` |
| `gcp-cloud-build/` | Sequential Cloud Build steps ordered with `waitFor` | `python3 gcp-cloud-build/validate.py` |
| `teamcity-circleci-awareness/` | The same job as TeamCity Kotlin DSL and as a CircleCI config | `python3 teamcity-circleci-awareness/validate.py` |

## Prerequisites

- Python 3 with PyYAML (`pip install pyyaml`).
- No engine, cloud account or Maven project is needed: nothing here is executed on a real CI server.

## How to read it

Start with `gitlab-ci/`, then open `tekton/` and `argo-workflows/` to see how container-native engines express the same three steps. Each folder is standalone and its README lists what was and was not run.

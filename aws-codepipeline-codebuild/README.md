# aws-codepipeline-codebuild

A CodeBuild `buildspec.yml` that runs the Maven build, and a `pipeline.json` that wires a source stage to a build stage in CodePipeline.

## Goal

Show the AWS split: CodeBuild describes the build commands, CodePipeline describes the stages around it.

## Run it

```
python3 validate.py
```

Expected output: `aws-codepipeline-codebuild OK`.

Not run end to end: it needs a real AWS account, a CodeBuild project and a source connection. Nothing was deployed. `validate.py` only parses both files and asserts the structure.

## What it proves

- `buildspec.yml` (version 0.2) installs `corretto21`, runs `mvn -B -ntp compile` and `verify` in the build phase, and `-DskipTests package` in `post_build`.
- Test reports are read from `target/surefire-reports/*.xml` as JUnit XML, and `target/*.jar` is the artifact.
- `pipeline.json` has two stages, `Source` (a CodeStar connection to `main`) and `Build` (the CodeBuild project `orders-build`).
- The role, bucket and connection use the dummy account id `000000000000`; `validate.py` checks that no real account id is in the role ARN.

## Trade-offs

- Here the whole build, test, package flow is one CodeBuild job, so there are no separate stages as in the other folders.
- The dummy ARNs, bucket and `owner/orders` repository id must be replaced before any real use.
- The CodeBuild project itself and the IAM role are not defined here; they would need separate infrastructure code.

## When not to use it

- If you are not on AWS, the integrations (CodeStar connections, S3 artifact store) bring nothing.
- For complex multi-stage flows, this single-job build hides the steps from the pipeline view.

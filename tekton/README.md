# tekton

A Tekton `Task` that runs Maven and a `Pipeline` named `orders-ci` that chains it three times, in one `pipeline.yaml`.

## Goal

Show how Tekton splits reusable work (the `Task`) from orchestration (the `Pipeline`), using the same build, test, package flow as the other folders.

## Run it

```
python3 validate.py
```

Expected output: `tekton OK`.

Not run end to end: it needs a Kubernetes cluster with Tekton Pipelines installed, and none was used. `validate.py` only parses the YAML and asserts the structure.

## What it proves

- The `maven` Task takes a `goals` parameter and a `source` workspace, and runs `mvn -B -ntp $(params.goals)` in the `maven:3.9.9-eclipse-temurin-21` image.
- The Pipeline has the tasks `build`, `test`, `package`, all pointing at the same Task through `taskRef`.
- Order comes from `runAfter` (`test` after `build`, `package` after `test`); `validate.py` checks that every task after the first has it.
- Goals are `compile`, `verify` and `-DskipTests package`.

## Trade-offs

- A shared workspace is declared but nothing here provides it: a `PipelineRun` with a volume claim and a step that clones the code is still needed.
- Parametrising the goals keeps one Task, but hides what each pipeline step really does behind a string.
- Test reports and artifacts are not wired up, unlike the GitLab and Azure folders.

## When not to use it

- If you have no Kubernetes cluster, Tekton's setup cost outweighs the benefit.
- For simple builds on a hosted service, a managed engine in the other folders is less work.

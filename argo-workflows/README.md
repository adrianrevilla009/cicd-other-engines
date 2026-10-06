# argo-workflows

An Argo `Workflow` in `workflow.yaml` that runs build, test and package as a DAG over one container template.

## Goal

Show the build, test, package flow as an Argo Workflows DAG, where order comes from `dependencies` and one template is reused with different parameters.

## Run it

```
python3 validate.py
```

Expected output: `argo-workflows OK`.

Not run end to end: it needs a cluster with Argo Workflows installed, and none was used. `validate.py` only parses the YAML and asserts the structure.

## What it proves

- The entrypoint `ci` is a `dag` with tasks `build`, `test`, `package`, in that order.
- `test` depends on `build` and `package` depends on `test`; `validate.py` asserts both.
- Every task points to the `mvn` template, which runs `mvn -B -ntp {{inputs.parameters.goals}}` in `maven:3.9.9-eclipse-temurin-21`.
- `generateName: orders-ci-` gives each submitted run a unique name.

## Trade-offs

- A DAG is more flexible than a plain list of steps, but here it is a straight chain, so the flexibility is unused.
- No volume or artifact is declared, so the three containers do not share a checkout. A real run needs a volume claim or an artifact repository.
- Each task starts its own pod, which costs startup time compared with one job running three commands.

## When not to use it

- For linear builds with no fan-out, a simpler engine is enough.
- If your team has no cluster operations skills, a hosted CI service is easier to run.

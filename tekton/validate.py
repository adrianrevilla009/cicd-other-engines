"""Offline structural check of the shared pipeline shape (build -> test -> package)."""
import yaml, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

docs = list(yaml.safe_load_all(open("pipeline.yaml")))
task = next(d for d in docs if d["kind"] == "Task")["metadata"]["name"]
pipe = next(d for d in docs if d["kind"] == "Pipeline")["spec"]["tasks"]
assert [t["name"] for t in pipe] == ["build", "test", "package"]
assert all(t["taskRef"]["name"] == task for t in pipe)
assert all("runAfter" in t for t in pipe[1:])
print("tekton OK")

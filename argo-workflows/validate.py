"""Offline structural check of the shared pipeline shape (build -> test -> package)."""
import yaml, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

wf = yaml.safe_load(open("workflow.yaml"))["spec"]
tpl = {t["name"]: t for t in wf["templates"]}
assert wf["entrypoint"] in tpl
tasks = {t["name"]: t for t in tpl["ci"]["dag"]["tasks"]}
assert list(tasks) == ["build", "test", "package"]
assert tasks["test"]["dependencies"] == ["build"] and tasks["package"]["dependencies"] == ["test"]
assert all(t["template"] in tpl for t in tasks.values())
print("argo-workflows OK")

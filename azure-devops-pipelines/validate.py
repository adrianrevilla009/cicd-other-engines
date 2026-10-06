"""Offline structural check of the shared pipeline shape (build -> test -> package)."""
import yaml, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

d = yaml.safe_load(open("azure-pipelines.yml"))
st = d["stages"]
assert [s["stage"] for s in st] == ["build", "test", "package"]
assert st[1]["dependsOn"] == "build" and st[2]["dependsOn"] == "test"
assert all(s["jobs"] for s in st)
print("azure-devops-pipelines OK")

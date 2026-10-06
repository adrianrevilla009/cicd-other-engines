"""Offline structural check of the shared pipeline shape (build -> test -> package)."""
import yaml, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

d = yaml.safe_load(open(".gitlab-ci.yml"))
assert d["stages"] == ["build", "test", "package"]
for s in d["stages"]:
    jobs = [k for k, v in d.items() if isinstance(v, dict) and v.get("stage") == s]
    assert jobs, f"no job in stage {s}"
assert "mvn" in " ".join(d["test"]["script"])
print("gitlab-ci OK")

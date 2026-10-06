"""Offline structural check of the shared pipeline shape (build -> test -> package)."""
import yaml, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

d = yaml.safe_load(open("cloudbuild.yaml"))
assert [s["id"] for s in d["steps"]] == ["build", "test", "package"]
for prev, s in zip(d["steps"], d["steps"][1:]):
    assert s["waitFor"] == [prev["id"]]
assert d["artifacts"]["objects"]["location"].startswith("gs://placeholder")
print("gcp-cloud-build OK")

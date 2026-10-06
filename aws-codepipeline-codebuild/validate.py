"""Offline structural check of the shared pipeline shape (build -> test -> package)."""
import yaml, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import json
b = yaml.safe_load(open("buildspec.yml"))
assert b["version"] == 0.2 and b["phases"]["build"]["commands"]
assert "package" in b["phases"]["post_build"]["commands"][0]
p = json.load(open("pipeline.json"))["pipeline"]
assert [s["name"] for s in p["stages"]] == ["Source", "Build"]
assert "000000000000" in p["roleArn"]  # placeholder account only
print("aws-codepipeline-codebuild OK")

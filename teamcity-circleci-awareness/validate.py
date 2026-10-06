"""Offline structural check of the shared pipeline shape (build -> test -> package)."""
import yaml, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import re
c = yaml.safe_load(open(".circleci/config.yml"))
run = [s["run"] for s in c["jobs"]["build-test-package"]["steps"] if isinstance(s, dict) and "run" in s]
assert len(run) == 3 and "verify" in run[1]
k = open(".teamcity/settings.kts").read()
assert re.findall(r'goals = "([^"]+)"', k) == ["compile", "verify", "-DskipTests package"]
print("teamcity-circleci-awareness OK")

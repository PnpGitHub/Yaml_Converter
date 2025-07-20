from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import LiteralScalarString
from io import StringIO

def convert_with_basic_mapper(gitlab_yaml: str) -> str:
    try:
        yaml_in = YAML()
        yaml_in.preserve_quotes = True
        data = yaml_in.load(gitlab_yaml)

        github_yaml = {
            "name": "CI",
            "on": ["push", "pull_request"],
            "jobs": {}
        }

        for job_name, job in data.items():
            if job_name == "stages":
                continue

            job_dict = {
                "runs-on": "ubuntu-latest",
                "steps": [
                    {"uses": "actions/checkout@v2"},
                ]
            }

            image = job.get("image", "")
            if "python" in image:
                job_dict["steps"].append({
                    "uses": "actions/setup-python@v2",
                    "with": {"python-version": image.split(":")[-1]}
                })

            script = job.get("script", [])
            if script:
                job_dict["steps"].append({
                    "name": "Run Script",
                    "run": LiteralScalarString("\n".join(script))  # ✅ Proper block format
                })

            github_yaml["jobs"][job_name] = job_dict

        # Dump to string
        yaml_out = YAML()
        yaml_out.preserve_quotes = True
        yaml_out.default_flow_style = False

        stream = StringIO()
        yaml_out.dump(github_yaml, stream)
        return stream.getvalue()

    except Exception as e:
        return f"# Error during conversion: {e}"

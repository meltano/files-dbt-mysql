from setuptools import setup, find_packages

setup(
    name="files-dbt-mysql",
    version="0.1",
    description="Meltano project files for dbt-mysql",
    packages=find_packages(),
    package_data={
        "bundle": [
            "transform/.gitignore",
            "transform/dbt_project.yml",
            "transform/models/.gitkeep",
            "transform/profiles/mysql/profiles.yml",
        ]
    },
)

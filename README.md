# files-dbt-mysql

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) for [dbt](https://www.getdbt.com/).

Files:

- [`transform/models`](./bundle/transform/models) (directory)
- [`transform/profiles/mysql/profiles.yml`](./bundle/transform/profiles/mysql/profiles.yml)
- [`transform/dbt_project.yml`](./bundle/transform/dbt_project.yml)
- [`transform/.gitignore`](./bundle/transform/.gitignore)

```bash
# Add dbt-mysql transformer and this file bundle to your Meltano project
meltano add transformer dbt-mysql

# Add only this file bundle to your Meltano project
meltano add files dbt-mysql
```

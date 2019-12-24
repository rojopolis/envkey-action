# envkey-action
GitHub Action to configure workflow with environment from EnvKey (https://www.envkey.com/)

## Usage:
```yaml
on: push

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Configure Environment
      env:
        ENVKEY: ${{ secrets.ENVKEY }}
      uses: rojopolis/envkey-action@master
    - name: Show environment
      run: env
```

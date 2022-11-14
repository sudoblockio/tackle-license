# tackle-license

A [tackle-box](https://github.com/robcxyz/tackle-box) provider to generate a license file in a directory. 

Licenses Supported:

- Apache 2.0
- MIT
- GPL-V3
- BSD
- Closed Source

## Usage 

Within a **`tackle.yaml`**:
```yaml
project_slug->: input 
compact->: tackle robcxyz/tackle-license --output {{project_slug}}
expanded:
  _>: tackle robcxyz/tackle-license 
  output: {{project_slug}}
```

From command line:
```shell
tackle robcxyz/tackle-license
```

### License

[Apache 2.0](LICENSE)
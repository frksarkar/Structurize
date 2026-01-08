# 🧱 Structurize

**Structurize** is a config-driven Python tool that generates complete project folder and file structures from human-readable templates such as `.tree` and `.json` files.

It helps developers scaffold complex projects quickly, consistently, and without repetitive manual setup.

## ✨ Key Features

- 📂 Generate folders & files automatically
- 🌳 Supports `.tree` (ASCII tree) format
- 🧩 Supports `.json` structure format
- ⚙️ YAML-based configuration
- 📝 Inline documentation support
- 🔁 Multi-file template support
- 🧪 Dry-run mode for safe preview
- 🧱 Modular & extensible architecture
- 🚀 Designed for large-scale projects & monorepos


## 📦 Supported Template Formats

### 1️⃣ `.tree` (Indentation / ASCII Tree)

```tree
    project/
    ├── src/
    │   ├── main.py
    │   └── utils/
    │       └── helper.py
    └── README.md
```

### 2️⃣ `.json` (Nested Structure)

```json
    {
        "project": {
            "src": {
                "main.py": {},
                "utils": {
                    "helper.py": ""
                }
            },
            "README.md": {}
        }
    }
```

## 🛠 Configuration Example

 ```yaml
    path:
    output_dir: output
    working_dir: structure
    file_path: indentation.tree

    mode: dry-run           # normal | dry-run | verbose
    multi_file_mode: true
    indent: 4
    read_file_extension: tree

    doc_separator: '##'
```


## ▶️ Usage


1️⃣ Install dependencies
```bash
    pip install -r requirements.txt
```

2️⃣ Run the generator
```bash
    python src/main.py
```

Generated output will appear in the configured `output_dir.`

## 🚀 How It Works

1. Reads configuration from config.yaml
2. Detects template files (.tree / .json)
3. Parses structure & documentation
4. Validates paths and filenames
5. Generates folders and files
6. Injects inline documentation when available




## 🌱 Future Improvements

CLI support (structurize init)
- Feature registry system
- Template variables ({{project_name}})
- Plugin architecture
- Improved logging & error handling
- PyPI package release

## 🤝 Contributing

- Contributions are welcome!🎉

## 📜 License
This project is open source and available under the MIT License.

## 👤 Author

- [Omar Faruk Sarkar](https://github.com/FarukSarkar)
- GitHub: https://github.com/FarukSarkar
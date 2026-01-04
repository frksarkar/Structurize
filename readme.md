# 📁 Python Project Structure & Template Generator

A clean, configurable, and extensible Python tool to automatically generate folder structures and files from templates using configuration files.

This project is designed to help developers scaffold projects faster, maintain consistency, and avoid repetitive setup work.

---

## ✨ Features

- 📂 Automatic folder & file structure generation
- 📄 Template-based file creation
- ⚙️ YAML configuration support
- 🧹 Text cleaning & validation utilities
- 🧱 Modular and scalable architecture
- 🧪 Test-ready structure
- 🧩 Easy to extend for new project types

---


## 🚀 How It Works

1. Define your project structure and templates in `config/config.yaml`
2. Run the main script
3. The tool:
   - Validates configuration
   - Builds folder structure
   - Parses templates
   - Cleans and writes output files

---

## ▶️ Usage

```bash
    pip install -r requirements.txt
    python src/main.py
```
Generated output will be available in the output/ directory.

---

## 🛠 Configuration Example

 ```yaml
    project_name: my_project
    path:
        output_dir: output
        working_dir: structure
        file_path: structure.tree
    mode: dry-run
```

## 🌱 Future Improvements

- CLI support (argparse / click)
- Multiple template presets
- JSON config support
- Plugin system for custom generators
- Better error reporting
- Rich logging

## 🤝 Contributing

- Contributions are welcome!🎉

## 📜 License
This project is open source and available under the MIT License.

## 👤 Author

- [Omar Faruk Sarkar](https://github.com/FarukSarkar)
- GitHub: https://github.com/FarukSarkar
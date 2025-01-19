#!/usr/bin/env python3

import os
import subprocess
import argparse
from typing import List
from pathlib import Path


def export_html_wasm(notebook_path: str, output_dir: str, as_app: bool = False) -> bool:
    """Export a single marimo notebook to HTML format.

    Returns:
        bool: True if export succeeded, False otherwise
    """
    output_path = notebook_path.replace(".py", ".html")

    cmd = ["marimo", "export", "html-wasm"]
    if as_app:
        print(f"Exporting {notebook_path} to {output_path} as app")
        cmd.extend(["--mode", "run", "--no-show-code"])
    else:
        print(f"Exporting {notebook_path} to {output_path} as notebook")
        cmd.extend(["--mode", "edit"])

    try:
        output_file = os.path.join(output_dir, output_path)
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        cmd.extend([notebook_path, "-o", output_file])
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error exporting {notebook_path}:")
        print(e.stderr)
        return False
    except Exception as e:
        print(f"Unexpected error exporting {notebook_path}: {e}")
        return False


def generate_index(all_notebooks: List[str], output_dir: str) -> None:
    """Generate the index.html file."""
    print("Generating index.html")

    index_path = os.path.join(output_dir, "index.html")
    os.makedirs(output_dir, exist_ok=True)

    try:
        with open(index_path, "w") as f:
            f.write(
                """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Marimo Notebooks</title>
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body class="bg-gray-50 dark:bg-gray-900" x-data="{ darkMode: false }">
    <div class="max-w-4xl mx-auto p-8">
      <nav class="flex justify-between items-center mb-12">
        <img src="https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/marimo-logotype-thick.svg" 
             alt="marimo" 
             class="h-12 dark:invert" />
        <button @click="darkMode = !darkMode" 
                class="p-2 rounded-lg bg-gray-200 dark:bg-gray-700">
          <span x-show="!darkMode">🌙</span>
          <span x-show="darkMode">☀️</span>
        </button>
      </nav>
      <div class="grid md:grid-cols-2 gap-6">
"""
            )
            for notebook in all_notebooks:
                notebook_name = notebook.split("/")[-1].replace(".py", "")
                display_name = notebook_name.replace("_", " ").title()
                is_app = notebook.startswith("apps/")

                f.write(
                    f'''      <div class="group p-6 bg-white dark:bg-gray-800 rounded-xl shadow-sm hover:shadow-md transition-all">
          <div class="flex justify-between items-start mb-4">
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white">{display_name}</h3>
            <span class="px-2 py-1 text-xs rounded-full {'bg-blue-100 text-blue-800' if is_app else 'bg-green-100 text-green-800'}">
              {('App' if is_app else 'Notebook')}
            </span>
          </div>
          <a href="{notebook.replace('.py', '.html')}" 
             class="inline-flex items-center px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 focus:ring-4 focus:ring-indigo-300 transition-colors">
            Open {('App' if is_app else 'Notebook')}
            <svg class="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </a>
        </div>\n'''
                )
            f.write(
                """      </div>
    </div>
    <script>
      if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.classList.add('dark')
      }
    </script>
  </body>
</html>"""
            )
    except IOError as e:
        print(f"Error generating index.html: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build marimo notebooks")
    parser.add_argument(
        "--output-dir", default="_site", help="Output directory for built files"
    )
    args = parser.parse_args()

    all_notebooks: List[str] = []
    for directory in ["notebooks", "apps"]:
        dir_path = Path(directory)
        if not dir_path.exists():
            print(f"Warning: Directory not found: {dir_path}")
            continue

        all_notebooks.extend(str(path) for path in dir_path.rglob("*.py"))

    if not all_notebooks:
        print("No notebooks found!")
        return

    # Export notebooks sequentially
    for nb in all_notebooks:
        export_html_wasm(nb, args.output_dir, as_app=nb.startswith("apps/"))

    # Generate index only if all exports succeeded
    generate_index(all_notebooks, args.output_dir)


if __name__ == "__main__":
    main()
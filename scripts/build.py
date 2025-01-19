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
    <title>Active Inference Learning Path</title>
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <script>
      // Add Tailwind dark mode configuration
      tailwind.config = {
        darkMode: 'class'
      }
    </script>
  </head>
  <body class="bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800 min-h-screen" 
        x-data="{ 
          darkMode: localStorage.getItem('darkMode') === 'true',
          activeTab: 'all',
          toggleDark() {
            this.darkMode = !this.darkMode;
            localStorage.setItem('darkMode', this.darkMode);
            if (this.darkMode) {
              document.documentElement.classList.add('dark');
            } else {
              document.documentElement.classList.remove('dark');
            }
          }
        }"
        x-init="$watch('darkMode', value => {
          if (value) {
            document.documentElement.classList.add('dark');
          } else {
            document.documentElement.classList.remove('dark');
          }
        });
        if (darkMode) document.documentElement.classList.add('dark');">
    
    <!-- Header -->
    <header class="border-b dark:border-gray-700 bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm fixed w-full z-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center py-4">
          <div class="flex items-center space-x-8">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/ec/Brain.svg" 
                 alt="brain symbol" 
                 class="h-8 dark:invert" />
          </div>
          <div class="flex items-center space-x-4">
            <button @click="toggleDark()"
                    class="p-2 rounded-lg bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors">
              <i class="fas" :class="darkMode ? 'fa-sun' : 'fa-moon'"></i>
            </button>
            <a href="https://github.com/skoghoern/skoghoern.github.io" 
               class="text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white">
              <i class="fab fa-github text-xl"></i>
            </a>
          </div>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="pt-24 pb-12 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
      <!-- Hero Section -->
      <div class="text-center mb-16">
        <h1 class="text-4xl font-bold text-gray-900 dark:text-white mb-4">
          Learn Active Inference
        </h1>
        <p class="text-lg text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
          Explore interactive notebooks and learn about Active Inference, from basic concepts to advanced applications.
        </p>
      </div>

      <!-- Filter Tabs -->
      <div class="flex justify-center mb-8 space-x-4">
        <button @click="activeTab = 'all'"
                :class="{ 'bg-indigo-100 dark:bg-indigo-900 text-indigo-700 dark:text-indigo-300': activeTab === 'all', 'text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white': activeTab !== 'all' }"
                class="px-4 py-2 rounded-lg text-sm font-medium transition-colors">
          All
        </button>
        <button @click="activeTab = 'intro'"
                :class="{ 'bg-indigo-100 dark:bg-indigo-900 text-indigo-700 dark:text-indigo-300': activeTab === 'intro', 'text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white': activeTab !== 'intro' }"
                class="px-4 py-2 rounded-lg text-sm font-medium transition-colors">
          Introduction
        </button>
        <button @click="activeTab = 'advanced'"
                :class="{ 'bg-indigo-100 dark:bg-indigo-900 text-indigo-700 dark:text-indigo-300': activeTab === 'advanced', 'text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white': activeTab !== 'advanced' }"
                class="px-4 py-2 rounded-lg text-sm font-medium transition-colors">
          Advanced
        </button>
      </div>

      <!-- Notebooks Grid -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
"""
            )
            # Group notebooks by category
            for notebook in all_notebooks:
                notebook_name = notebook.split("/")[-1].replace(".py", "")
                display_name = notebook_name.replace("_", " ").title()
                is_app = notebook.startswith("apps/")
                category = "intro" if "intro" in notebook_name.lower() else "advanced"

                f.write(
                    f'''        <div x-show="activeTab === 'all' || activeTab === '{category}'"
             class="group bg-white dark:bg-gray-800 rounded-xl shadow-sm hover:shadow-lg transition-all duration-300 overflow-hidden"
             x-transition:enter="transition ease-out duration-300"
             x-transition:enter-start="opacity-0 transform scale-95"
             x-transition:enter-end="opacity-100 transform scale-100">
          <div class="p-6">
            <div class="flex justify-between items-start mb-4">
              <h3 class="text-xl font-semibold text-gray-900 dark:text-white">{display_name}</h3>
              <span class="px-3 py-1 text-xs font-medium rounded-full {'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-300' if is_app else 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300'}">
                {('App' if is_app else 'Notebook')}
              </span>
            </div>
            <p class="text-gray-600 dark:text-gray-400 mb-4 text-sm">
              {category.title()} level notebook about Active Inference concepts.
            </p>
            <a href="{notebook.replace('.py', '.html')}" 
               class="inline-flex items-center px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 focus:ring-4 focus:ring-indigo-300 transition-colors w-full justify-center">
              Open Notebook
              <i class="fas fa-arrow-right ml-2 group-hover:translate-x-1 transition-transform"></i>
            </a>
          </div>
        </div>\n'''
                )
            f.write(
                """      </div>
    </main>

    <!-- Footer -->
    <footer class="bg-white dark:bg-gray-900 border-t dark:border-gray-800">
      <div class="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
        <div class="text-center text-gray-600 dark:text-gray-400 text-sm">
          Built with <i class="fas fa-heart text-red-500"></i> using Marimo Notebooks
        </div>
      </div>
    </footer>

    <script>
      // Initialize dark mode from localStorage or system preference
      if (localStorage.getItem('darkMode') === null && window.matchMedia('(prefers-color-scheme: dark)').matches) {
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
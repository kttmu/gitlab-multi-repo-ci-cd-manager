import os
import subprocess
import yaml
import networkx as nx
from scripts.dependency_graph import build_dependency_graph
from scripts.version_manager import manage_versions

# 設定ファイルの読み込み
def load_config():
    with open('config/settings.yaml', 'r') as file:
        return yaml.safe_load(file)

def run_tests(repo_path):
    print(f"Running tests for {repo_path}")
    subprocess.run(["pytest", repo_path], check=True)

def build_project():
    print("Building C++ project...")
    subprocess.run(["./build.sh"], check=True)

def main():
    config = load_config()
    repositories = config['repositories']

    # バージョン管理
    manage_versions(repositories)
    
    # 依存関係グラフの生成
    dependency_graph = build_dependency_graph(repositories)

    # ビルド実行
    build_project()

    # テストの自動実行
    for repo in nx.topological_sort(dependency_graph):
        repo_path = repositories[repo]['path']
        run_tests(repo_path)



if __name__ == '__main__':
    main()

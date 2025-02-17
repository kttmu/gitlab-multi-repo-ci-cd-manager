# 🌐 GitLab CI/CDを用いたマルチレポジトリ管理ツール

## 🚀 プロジェクト概要

このプロジェクトは、**複数のGitLabリポジトリをまとめて管理し、依存関係を考慮したCI/CDを構築するツール**です。
このリポジトリをフォークしてプロジェクトごとにカスタマイズして利用することを想定しています。

✅ **主な機能:**
- 複数のリポジトリを統合的にビルド・テスト。
- ブランチがpushされた際に自動的にテストを実行。
- テストレポートの差分を検出し、差分がなければ自動マージ。
- メール通知によるフィードバック。
- QACを用いた静的解析を含む複数のテストを実施。

---

## 📁 フォルダ構成

```
/
├── main.py                 # CI/CDパイプラインの統合実行ファイル
├── build.sh                 # C++プロジェクトのビルド実行スクリプト
├── submodule.txt            # 統合対象のリポジトリ一式を記載するモジュールリスト
├── run_**.sh                # テスト用のシェルスクリプト
├── config/
│   └─ settings.yaml         # CI/CDパイプラインの設定ファイル
├── scripts/
│   ├─ dependency_graph.py   # 依存関係グラフの生成ロジック
│   └─ version_manager.py    # バージョン管理スクリプト
├── CMakeLists.txt            # C++プロジェクトのビルド設定ファイル
├── requirements.txt          # Python依存ライブラリ一覧
├── .gitlab-ci.yml             # CI/CDパイプライン設定ファイル
├── reports/                   # テストレポート保存用ディレクトリ
└── README.md                 # 本ドキュメント
```

---

## 🔧 セットアップ手順

1. **リポジトリをクローンします。**

```bash
git clone https://your-gitlab-repo-url.git
cd your-repo-name
```

2. **依存関係をインストールします。**

```bash
pip install -r requirements.txt
```

3. **初回ビルドを実行します。**

```bash
bash build.sh
```

4. **CI/CDの設定を有効化します。**

- GitLabでリポジトリの `Settings -> CI/CD -> Pipeline triggers` に移動し、パイプライントリガーを作成します。
- `Settings -> Webhooks` に移動し、ブランチのpushを検知してCI/CDをトリガーするためのURLを登録します。

---

## ⚙️ 使用技術

- **プログラミング言語:** Python, C++
- **ビルドツール:** CMake
- **CI/CD:** GitLab CI/CD
- **静的解析:** QAC
- **テスト:** Google Test（単体テスト・カバレッジ）、ブラックボックステスト、機能テスト
- **通知:** メール（差分あり・なしをレポート）

---

## 📊 CI/CDパイプラインの流れ

1️⃣ **ビルドステージ:**
- C++プロジェクトをビルドし、成果物を保存。

2️⃣ **テストステージ:**
- 静的解析（QAC）
- 単体テスト（Google Test）
- 状態遷移テスト（ブラックボックステスト）
- 機能テスト

3️⃣ **レポート差分確認ステージ:**
- レポートの差分を自動検出。
- 差分がなければ自動マージ。
- 差分があればメールで通知。

---

## 📩 通知機能について

✅ テストレポートに前回との差分がない場合 → 自動マージ。  
✅ 差分がある場合 → メールで通知（レポートの確認を促します）。

---

## 📈 今後の展望

✨ CI/CDパイプラインの高速化。  
✨ コンテナ化対応（Docker）による環境の統一。  
✨ Jira連携によるタスクトラッキングの自動化。

---

## 👥 コントリビューション

- バグ報告や機能追加のリクエストは、Issuesを活用してください！
- プルリクエストは大歓迎です！

---

🔥 **このツールで複数のリポジトリを一括管理し、車載ソフトウェア開発の効率化を実現しましょう！** 🚀




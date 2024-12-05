# Bedrock Prompt Router Demo

Amazon Bedrock Intelligent Prompt Routingを使用するデモプログラムです。

## 概要

このデモでは、Amazon Bedrockのプロンプトルーター機能を使用して、適切なFoundation Modelに自動的にリクエストをルーティングする方法を示します。

### 特徴
- プロンプトの複雑さに応じて最適なモデルを自動選択
- コストとパフォーマンスの最適化
- 使用されたモデルの確認が可能

## 前提条件

- Python 3.8以上
- AWS認証情報の設定
- 必要なIAMポリシー
  - `bedrock:ListPromptRouters`
  - `bedrock:GetPromptRouter`
  - `bedrock-runtime:InvokeModel`

## セットアップ

1. リポジトリのクローン
```bash
git clone https://github.com/yourusername/bedrock-prompt-router-demo.git
cd bedrock-prompt-router-demo
```

2. 仮想環境の作成と有効化
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# または
.\venv\Scripts\activate  # Windows
```

3. 依存関係のインストール
```bash
pip install -r requirements.txt
```

4. AWS認証情報の設定
```bash
aws configure
```

## 使用方法

1. `src/bedrock-prompt-router-demo.py`の以下の部分を編集:
```python
# プロンプトルーターのARNを指定
ROUTER_ARN = "<YOUR_PROMPT_ROUTER_ARN>"

# メッセージの作成
messages = [{
    "role": "user",
    "content": [
        {"text": "<YOUR_QUESTION>"}
    ]
}]
```

2. スクリプトの実行:
```bash
python src/bedrock-prompt-router-demo.py
```

## 注意事項

- プロンプトルーターは現在プレビュー段階です
- 利用可能なリージョン:
  - us-east-1 (バージニア北部)
  - us-west-2 (オレゴン)
- 現在は英語のプロンプトのみサポート
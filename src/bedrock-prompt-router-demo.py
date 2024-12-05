import json
import boto3

# Bedrockクライアントの初期化
bedrock_runtime = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

# プロンプトルーターのARNを指定
ROUTER_ARN = "<YOUR_PROMPT_ROUTER_ARN>"

# メッセージの作成
messages = [{
    "role": "user",
    "content": [
        {"text": "<YOUR_QUESTION>"}
    ]
}]

# プロンプトルーターを使用してモデルを呼び出し
response = bedrock_runtime.converse(
    modelId=ROUTER_ARN,
    messages=messages
)

# レスポンスの表示
print("Response:")
print(response["output"]["message"]["content"][0]["text"])

# 使用されたモデルの確認
print("\nUsed Model:")
print(json.dumps(response["trace"], indent=2))
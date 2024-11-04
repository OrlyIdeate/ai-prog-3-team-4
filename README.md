# チーム4

### アプリの起動方法

1. venv（仮想環境）を起動
    ```
    .\.venv\Scripts\activate

    ```
2. アプリ起動

    ```
    python app.py
    ```

### requirements.txtを使ったライブラリ管理
- requirements.txtのライブラリのインストール
    ```
    pip install -r requirements.txt
    ```
- requirements.txtのライブラリの追加
    ```
    pip freeze > requirements.txt
    ```
---

## プロジェクト名
    プロジェクトX

## チーム名とメンバー一覧
- 上野 迅 
- 城戸 俊介
- 久我 祐司
- 中島 千尋
- 甲斐 咲希人

## プロジェクトの概要（1-2文で簡潔に）
    生成AIを用いて、使って楽しい若い人に向けたwebアプリ

## 開発するアプリケーションの目的
    暇な時間に楽しめる生成AI App

## 想定されるターゲットユーザー
    10～20代

## 主な機能リスト
    - 画像生成
    - フィルター
    - 保存機能

## 使用予定の AI 技術や API
    OpenAI API
    Dall-E

## 技術スタック（プログラミング言語、フレームワーク、ライブラリなど）
    - Python
    - Flask
    - HTML
    - CSS

## 開発スケジュール（主要なマイルストーン）
    1. 画像生成機能実装
    2．生成した画像をダウンロード機能実装
    3. 生成した画像を編集する機能実装

## 各メンバーの役割分担

### フロントエンド
- 城戸 俊介 （画像生成部分）
- 久我 祐司 （フィルター）

### バックエンド
- 上野 迅   （画像生成部分）
- 中島 千尋 （フィルター）

## 想定される課題や困難点
    - 指示通りの画像が生成されない
    - 生成した画像へのフィルターの適用

## プロジェクトの成功基準
    - 指示通りの画像が生成される
    - フィルターの適用ができる

## 将来の拡張可能性
    - 各ジャンルの画像が生成できる（アニメ調, 写真風 etc...）

## 参考資料
aaaa

# CentralSystems
混雑度情報を管理する中央システムです。

# DEMO
- [利用イメージ動画](https://www.youtube.com/watch?v=2ZZNa0-mkMA&t=2s)


# Requirement
[Docker環境](https://github.com/s-project2021/CentralSystem_DevelopEnv)
* Python 3.9.6
* Django 3.2.5  

# Installation
```sh
python manage.py makemigrations
python manage.py migrate
```

# Run
```sh
python manege.py runserver
```

# Usage
## pass
- /：ホーム画面
- /crowd/syokuji/：食事の混雑状況
- /crowd/kyukei/：休憩場所の混雑状況
- /crowd/pc/：パソコン室の混雑状況
- /menu/ikuta/：生田会館のメニュー
- /menu/green/：グリーントップのメニュー
- resultprocessing/message/：DBの混雑状況のデータを表示するパス(確認用)

# License　
- [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.txt)



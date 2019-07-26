- 初始化Django项目
    - django-admin startproject Django_tornado_server

- 数据库迁移
    - python manage.py makemigrations
    - python manage.py migrate
    
- 创建子应用
    - python manage.py startapp User
    - python manage.py startapp Profile
    
- pip导出，导入环境配置
    - pip freeze > requirements.txt
    - pip install -r requirements.txt
    
- conda导出,导入环境配置
    - conda env export --file requirements.yml
    - conda env create -f  requirements.yml
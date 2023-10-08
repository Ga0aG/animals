1. 增加物种
    1. 在[ompl.md](./ompl.md)文件中按照分类添加物种
    2. 更新目录，也就是更新_sidebar.md文档,打开终端 `python3 scripts/to_sidebar.py`
    3. 生成物种对应文档，`python3 scripts/create_files.py`
    4. 编辑文档
2. 上传更新
     1. 更新代码，切到开发分支
        1. 切到main分支`git checkout main`
        2. 拉一下最新代码`git pull origin main`
        3. 本地切到一个新的分支`git checkout <分支名>(分支名字自定义，一般以feature/开头)`
     2. 编辑内容提交代码
        1. 编辑内容
        2. `git add .`
        3. `git commit -m <简要描述更新内容>`
        4. 上传代码`git push origin <分支名>`
     3. 网上上提交合并请求pull request
3. 本地部署
   1. Windows
      1. 安装docsify
         1. 安装[nodejs](https://nodejs.org/en/download)
         2. Custom setup选择Add to path
         3. 安装好后打开终端，npm -v有显示版本号表示成功接着下一步
         4. npm i docsify-cli -g
         5. 管理员权限运行power shell, 输入`set-ExecutionPolicy RemoteSigned`, 选择Y
      2. 在animals目录下，`docsify serve .`
      3. 网页上访问http://localhost:3000
4. 多平台协作
   1. Windows
      1. `cd animals`
      2. `git config core.autocrlf true`
      3. `git config core.fileMode false`
5. 内容更新rules
   1. 图片采用压缩过后的图片，方便加载
   2. 图片以`01.<文件格式>`形式命名
   3. 文档的开头可放一张生物的示意图片，再开始属性描述
   4. 生僻字可加拼音，例: 蚰[yóu]蜒[yán]
   5. 以中文括号符开头描述不同生物的特性，例：[樽海鞘纲](动物界/脊索动物门/樽海鞘纲/樽海鞘纲.md)
   6. 内容出处放进参考里，例:

      ```
      参考:
      - [标题-用户名-平台](链接)
      ```

本网站用于记录个人学习笔记, 采用 [docsify](https://github.com/docsifyjs/docsify) 构建. 主要参考 [官方文档](https://docsify.js.org/#/); [ArchLinuxTutorial](https://github.com/ArchLinuxStudio/ArchLinuxTutorial). 

```sh
# see https://github.com/docsifyjs/docsify-cli
# install
npm i docsify-cli -g
# initial. 仅仅是创建了 index.html 和 README.md 和 .nojekyll 文件
docsify init ./docs

# serve at http://localhost:3000
docsify serve docs
# or use python 
cd docs && python -m http.server 3000
```

其中, initial 步骤仅仅是创建了 `index.html` 和 `README.md` 和 `.nojekyll` 文件. index.html 是入口文件 (entry file), README是主页 (home page), .nojekyll 防止 GitHub Pages 忽略下划线开头的文件. 

使用的插件

- [gittalk](https://github.com/gitalk/gitalk)
- [docsify-pagination](https://github.com/imyelo/docsify-pagination)

相关资源和插件

- [awesome](https://docsify.js.org/#/awesome) 🚩

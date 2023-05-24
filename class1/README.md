# 主题：Git & GitHub

## 腾讯会议回放链接：
[点这里](https://meeting.tencent.com/user-center/shared-record-info?id=98372a52-349d-466e-8f10-970a228be8a9) 
分享密码:NAvY


## Practice:
- fork本仓库，创建patch分支
- 将自己的学号和github id添加到Practice.md
- 提交PR，PR描述中请注明PR类型：**Practice PR**

注意： 不必接龙，跳号可以有效减少冲突。如果发生冲突，以时间最早的PR优先。

## Contributing:
我们开放一个笔记共创活动，具体笔记大纲已在TheNote.md中给出，同学们可以根据分享内容，结合自己的实践对教程进行补充（包括但不限于图文形式），补充过的同学可以获得仓库write权限。 

如果你决定认领或补充其中一个子板块，**请务必先提交issue**，在issue中说明你将要添加的内容，并与我们讨论。讨论通过后，再进行内容修改，然后提交PR（请在PR描述中引用讨论的issue链接，以便我们确认是经过讨论的）。**注意：未经讨论的PR是不被允许的。**

大致步骤如下：
1.在GitHub上Fork本仓库  
2.Clone Fork的个人仓库  
3.设置`upstream`仓库地址，并禁用`push`  
4.在个人仓库下创建新的开发分支，如`dev`分支  
5.PR之前保持与原仓库内容同步，然后再发起PR  

命令示例：
``` 
# fork
# clone
# 请将`zzyzeyuan`修改为你自己的UserName
git clone git@github.com:zzyzeyuan/EfficientTools.git

# set upstream
git remote add upstream git@github.com:DaSE4Good/EfficientTools.git
# disable upstream push
git remote set-url --push upstream DISABLE
# verify
git remote -v
# some sample output:
# origin	git@github.com:zzyzeyuan/EfficientTools.git (fetch)
# origin	git@github.com:zzyzeyuan/EfficientTools.git (push)
# upstream	git@github.com:DaSE4Good/EfficientTools.git(fetch)
# upstream	DISABLE (push)

# do your work on dev branch
git checkout -b dev
# edit and commit and push your changes
git push -u origin dev

# keep your fork up to date
## fetch upstream main and merge with forked main branch
git fetch upstream
git checkout main
git merge upstream/main
## rebase brach and force push
git checkout dev
git rebase main
git push -f
```

我们希望这个活动能对你的开源之路有一些帮助！！


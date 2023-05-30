# 主题：Docker

## 腾讯会议回放链接：



## Practice:
用Dockerfile构建一个镜像，并上传到DockerHub或GitHub Container Registry等镜像仓库。

满足以下要求**之一**：

- 使用”docker run 镜像名”运行时，打印一句话到终端中
- 启动一个web服务，浏览器访问时展示一句话

最后，

- 将**学号或姓名**、**运行镜像的命令**和项目的**代码仓库链接**添加到Practice.md
- 提交PR，PR描述中请注明PR类型：**Practice PR**

注意： 不必接龙，跳号可以有效减少冲突。如果发生冲突，以时间最早的PR优先。

*tips:*

*用docker login登录到镜像仓库后，docker push上传镜像。如果手头没有机器装Docker，可以使用[play with Docker](https://labs.play-with-docker.com/)在线试用, 或者使用[GitHub Action构建并上传](https://docs.docker.com/build/ci/github-actions/)。*

*参考的Dockerfile：*

```dockerfile
From alpine:3.18
CMD echo 今天我要吃蛋饼——VPCU
```

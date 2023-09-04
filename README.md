# 一、项目说明

## 1. 项目分支

### 1.1 dev

开发分支

### 1.2 release

发布分支

## 2. 项目结构

```
├── bin                                                  -- 可执行脚本目录
├── conf                                                 -- 配置目录
│   ├── datax                                        -- DataX相关配置目录
│   │   ├── config                               -- DataX`作业配置生成器`的配置文件目录
│   │   ├── datasource                           -- DataX`作业配置生成器`的配置文件所引用的`DataSource`目录
│   ├── flume                                      -- Flume作业配置目录
│   ├── hive                                       -- 数仓相关配置目录
│   └── template                                   -- 模板文件
│       ├── datax                                    -- DataX相关模板
│       ├── flume                                    -- Flume相关模板
│       └── hive                                     -- Hive相关模板
│   ├── validation                                 -- 数据校验相关配置目录
├── docs                                                 -- 文档
├── launch-pad                                           -- 上线区域
│   ├── ${project}                                   -- 项目名称
├── requirements.txt                                     -- 项目需要的Python包
├── workspace                                            -- 工作区域
--
└── lxy                                                  -- Python项目文件
```

## 3. 脚本用途与说明
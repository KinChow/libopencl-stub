libopencl-stub
==============

A stub opecl library that dynamically dlopen/dlsyms opencl implementations at runtime based on environment variables. Will be useful when opencl implementations are installed in non-standard paths (say pocl on android)



 LIBOPENCL_SO_PATH      -- Path to opencl so that will be searched first

 LIBOPENCL_SO_PATH_2    -- Searched second

 LIBOPENCL_SO_PATH_3    -- Searched third

 LIBOPENCL_SO_PATH_4    -- Searched fourth

 

Default paths will be searched otherwise



## Update
### 2024/6/22

更新代码，命令如下

```shell
git submodule update --init --recursive --remote
```



### 2024/2/3

更新编译脚本，使用python指令编译，支持编译Windows MSVC和Android静态库，命令如下

```shell
# 编译Windows静态库
python build.py --platform=Windows

# 编译Android静态库
python build.py --platform=Android

# 清理编译产物
python build.py --clean
```




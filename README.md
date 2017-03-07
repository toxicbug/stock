## 配置notepad++
* 点击插件>>Plugin Manager>>Show Plugin Manager>>Available
* 找到并在NppExec左边打上勾，然后点击Install即可。
* 按F6
* 输入
```
d:\Python27\python.exe "$(FULL_CURRENT_PATH)"
```
其中`d:\Python27\python.exe`需要换成自己的python安装路径，并且`$(FULL_CURRENT_PATH)`一定要用英文双引号引起来，并注意，`d:\Python25\python.exe`与`"$(FULL_CURRENT_PATH)"`中间有个空格
加入上述语句直接ok即可，或者点save，并给该操作命名，例如“RunPython”
* 下次编译时，可以对txt文件直接点击F6，点击OK进行编译
* 注意 每次编译前应先保存修改好的文件，不然编译器会编译修改前的文件，造成结果出错
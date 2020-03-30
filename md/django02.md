# 模版
- 模版：一组相同或者相似的页面，在需要个性化的地方进行六百，需要的的时候只是用数据填充就可以使用
- 步骤：
    - 1. 在setting中进行设置: TEMPLATES
    - 2. 在templates文件夹下编写模块并调用

## 模版-变量
- 变量的表示方法: {{var_name}}
- 在系统调用模版的时候，会用相应的数据查找相应的变量名称，如果能找到，
  则填充，或者叫渲染，否则，跳过
  
## 模版-标签
- for标签：{% for..in..%}
- 用法：
    {% for... in...%}
        循环语句
    {% endfor %} 案例three
    
## if标签
- 用来判断条件
- 代码实例：
    {% if 条件 %}
        条件成立执行语句
    {% else %}
        以上条件都不成立执行语句
    {% endif %}
    
## csrf标签
- csrf：跨站请求伪造
- 在提交表单的时候，表单页面需要加上{% scrf_token %}

# session
- 为了应对HTTP协议的无状态性
- 用来保存用户比较敏感的信息
- 属于request的一个属性
- 常用操作
    - request.session.get(key, defaultValue)
    - request.session.clear():清除全部
    - request.session[key]=  value:赋值
    - request.session.flush():删除当前回话且清除回话的cookie
    - del request.session[key]
    
#分页
- django提供现成的分页器用来对结果进行分页
- from django.core.paginator import Paginator

# Ajax

# 基于类的视图
- 可以针对http协议不同的方法创建不同的函数
- 可以使用Mixin等oop技术
- Mixin
    - 把来自父类的行为或者属性组合在一起
    - 解决多重继承问题
    
# admin
- 打开urls.py
- 创建超级用户
- 配置settings文件   

## 2.绑定管理模型

## 3.设置admin管理类
- 实现方式
    - ModelAdmin
    - 装饰器
- 修改页面显示数量：list_per_page
- 操作选项：actions_on_top/button
- 控制列表中显示的内容：list_display=[]
- 将方法作为列显示
    - 函数必须返回值
    - 设置short_descraption作为显示内容
    - 排序使用admin_order_field
- 关联对象
    - 使用方法
    
- 右侧过滤器

- 搜索框

- 分组显示
  

python

from flask import render_template, request, redirect, url_for, flash

from run import app

from models import init_db, get_all_items, add_item

from forms import ItemForm

初始化数据库

init_db()

@app.route('/')

def index():

items = get_all_items()

return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])

def add():

form = ItemForm()

if form.validate_on_submit():

add_item(form.name.data, form.category.data, form.quantity.data, form.location.data)

flash('物品添加成功！')

return redirect(url_for('index'))

return render_template('add.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])

def edit(id):

# 注意：这里为了演示，简化为直接传递参数，实际项目中可能需要从数据库查询原数据回填表单

form = ItemForm()

if form.validate_on_submit():

# 实际项目中这里应该有 update_item 函数

flash('物品修改成功！')

return redirect(url_for('index'))

return render_template('edit.html', form=form)

@app.route('/delete/<int:id>')

def delete(id):

# 实际项目中这里应该有 delete_item 函数

flash('物品删除成功！')

return redirect(url_for('index'))

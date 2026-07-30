python

from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, SubmitField

from wtforms.validators import DataRequired

class ItemForm(FlaskForm):

name = StringField('物品名称', validators=[DataRequired()])

category = StringField('分类')

quantity = IntegerField('数量', default=1)

location = StringField('存放位置')

submit = SubmitField('提交')

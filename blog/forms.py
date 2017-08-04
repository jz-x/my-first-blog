# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:22:08 2017

@author: Jerry
"""
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model=Post
        fields=('title','text')
        
        
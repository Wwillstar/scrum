#!/usr/bin/env python
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Sprint, Task

User = get_user_model()


class SprintSerializer(serializers.ModelSerializer):
    """使用序列化器，帮助API将模型序列化和串并转化"""
    links = serializers.SerializerMethodField()

    class Meta:
        model = Sprint
        fields = ('id', 'name', 'description', 'end','links',)

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('sprint-detail',
                kwargs={'pk': obj.pk}, request=request),
            'tasks':reverse('task-list',
                request=request)+'?sprint={}'.format(obj.pk),
        }


class TaskSerializer(serializers.ModelSerializer):
    assigned = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, required=False, allow_empty=True,
        queryset=User.objects.all())
    status_display = serializers.SerializerMethodField()  # 只读字段
    links = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'sprint',
                  'status', 'status_display', 'order',
                  'assigned', 'started', 'due', 'completed','links',)

    def get_status_display(self, obj):
        # 返回系列化器中get_status_display中方法的值，类似字典值而不是1，2,3,4
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        links= {
            'self': reverse('task-detail',
                kwargs={'pk': obj.pk}, request=request),
            'sprint':None,
            'assigned':None
        }
        if obj.sprint_id:
            links['sprint'] = reverse('sprint-detail',
                kwargs={'pk':obj.sprint_id},request=request)
        if obj.assigned:
            links['assigned'] = reverse('user-detail',
                kwargs={User.USERNAME_FIELD:obj.assigned},request=request)
        return links

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active','links',)

    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()
        return {
            'self': reverse('user-detail',
                kwargs={User.USERNAME_FIELD:username}, request=request),
            'tasks':'{}?assigned={}'.format(
                reverse('task-list',request=request),username)
        }
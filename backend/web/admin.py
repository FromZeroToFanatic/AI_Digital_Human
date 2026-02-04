from django.contrib import admin
from web.models.user import UserProfile
from web.models.character import Character

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',) #逗号不要删，其代表一个列表

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    raw_id_fields = ('author',)
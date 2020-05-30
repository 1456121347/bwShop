from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = '用户管理'
    def ready(self):
        import users.signals


 # #输入密码的时候不显示明文
 #    password = serializers.CharField(
 #        style={'input_type': 'password'},label=True,write_only=True
 #    )
 #
 #    #密码加密保存
 #    def create(self, validated_data):
 #        user = super(UserRegSerializer, self).create(validated_data=validated_data)
 #        user.set_password(validated_data["password"])
 #        user.save()
 #        return user